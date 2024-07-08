import cv2
import logging

# Configurer la journalisation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Charger le modèle pré-entraîné pour la détection des visages
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    logging.info("Début de la détection des visages.")
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Appliquer un histogramme d'égalisation pour améliorer le contraste
    gray = cv2.equalizeHist(gray)
    
    # Détecter les visages
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    logging.info("Fin de la détection des visages.")
    return frame

def main():
    logging.info("Démarrage de l'application.")
    # Initialiser la capture vidéo (0 pour la caméra par défaut)
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        logging.error("Erreur : Impossible d'ouvrir la caméra.")
        return
    
    logging.info("Caméra ouverte avec succès.")
    while True:
        # Lire une image de la caméra
        ret, frame = video_capture.read()
        
        if not ret:
            logging.error("Erreur : Impossible de lire une image de la caméra.")
            break
        
        # Détecter les visages dans l'image
        frame_with_faces = detect_faces(frame)
        
        # Afficher l'image avec les visages détectés
        cv2.imshow('Video', frame_with_faces)
        
        # Sortir de la boucle si la touche 'q' est appuyée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("Arrêt de l'application.")
            break
    
    # Libérer la capture vidéo et fermer les fenêtres
    video_capture.release()
    cv2.destroyAllWindows()
    logging.info("Application terminée.")

if __name__ == "__main__":
    main()
