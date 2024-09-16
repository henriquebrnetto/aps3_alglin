import numpy as np

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def transform_image(image, M):
    altura, largura, cores = image.shape
    X = image.reshape(altura*largura, cores).T
    image = (M @ X).T.reshape(altura, largura, cores)
    return image

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)
    FPS = cap.get(cv.CAP_PROP_FPS)

    # Controle de tempo
    t = 0

    # Velocidade angular (rotacoes por segundo)
    v = 0.2
    
    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320*2
    height = 240*2

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    expand = False
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break
        
        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        image_ = np.zeros_like(image)

        Xd = criar_indices(0, image.shape[0], 0, image.shape[1])
        Xd = np.vstack((Xd, np.ones(Xd.shape[1])))

        t += 1/FPS
        theta = v * t * 2 * np.pi
        cos = np.cos(theta)
        sen = np.sin(theta)

        rot = np.array([[cos, -sen, 0], [sen, cos, 0], [0, 0, 1]])
        move = np.array([[1, 0, -image.shape[0]/2], [0, 1, -image.shape[1]/2], [0, 0, 1]])

        if not expand:
            E = np.eye(3)

        M = np.linalg.inv(move) @ E @ rot @ move

        X = M @ Xd
        X = X.astype(int)
        Xd = Xd.astype(int)

        X[0,:] = np.clip(X[0,:], 0, image.shape[0]-1)
        X[1,:] = np.clip(X[1,:], 0, image.shape[1]-1)


        image_[Xd[0,:], Xd[1,:], :] = image[X[0,:], X[1,:], :]

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)

        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

        if cv.waitKey(1) == ord('a'):
            v *= 2
            t /=2
        
        if cv.waitKey(1) == ord('b'):
            v /= 2
            t *= 2
        
        if cv.waitKey(1) == ord('e'):
            E = np.array([[2, 0.5, 0], [0, 1, 0], [0, 0, 1]])
            expand = True
        
        if cv.waitKey(1) == ord('c'):
            expand = False

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
