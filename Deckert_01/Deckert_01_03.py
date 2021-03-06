# Deckert, Timothy
# 1000-637-406
# 2017-09-17
# Assignment_01_03

import numpy as np

class cl_world:
    def __init__(self, objects=[], canvases=[]):
        self.objects = objects
        self.canvases = canvases
        # self.display

    def add_canvas(self, canvas):
        self.canvases.append(canvas)
        canvas.world = self

    def create_graphic_objects(self, canvas, filename):
        file = open(filename, 'r')
        data = file.read()
        file.close()
	
        rows = data.splitlines()

        vertices = []
        faces = []

        for row in rows:

            row = row.strip()

            coords = row.split(" ")

            if coords[0] == "v":
                coords.append(1.0)
                coordMat = np.array(coords[1:], dtype=np.float32)
                vertices.append(coordMat)
            if coords[0] == "f":
                coordMat = np.array(coords[1:], dtype=np.int32)
                faces.append(coordMat)
            if coords[0] == "w":
                window = np.array(coords[1:], dtype=np.float32)
            if coords[0] == "s":
                viewport = np.array(coords[1:], dtype=np.float32)

        viewport[0] = int(viewport[0] * float(canvas.cget("width")))
        viewport[1] = int(viewport[1] * float(canvas.cget("height")))
        viewport[2] = int(viewport[2] * float(canvas.cget("width")))
        viewport[3] = int(viewport[3] * float(canvas.cget("height")))

        self.objects.append(canvas.create_rectangle(viewport[0], viewport[1], viewport[2], viewport[3], outline="red", width=2))

        vpx = (viewport[2] - viewport[0]) / (window[2] - window[0])
        vpy = (viewport[3] - viewport[1]) / (window[3] - window[1])

        dxy = np.array([[1,0,0,-window[0]],[0,-1,0,window[3]],[0,0,1,0],[0,0,0,1]])
        sxy = np.array([[vpx,0,0,0],[0,vpy,0,0],[0,0,1,0],[0,0,0,1]])
        dvpxy = np.array([[1,0,0,viewport[0]],[0,1,0,viewport[1]],[0,0,1,0],[0,0,0,1]])

        transform = np.dot(dvpxy, np.dot(sxy,dxy))
        
        particles = []

        for vertex in vertices:
            particles.append(np.dot(transform, vertex))

        points = []

        for face in faces:
            for fp in face:
                points.append(int(particles[int(fp)-1][0]))
                points.append(int(particles[int(fp)-1][1]))
        
            self.objects.append(canvas.create_polygon(points, outline="red", fill="yellow"))
            points = []

    def redisplay(self, canvas, event, width, height):
        if self.objects:
            points = []
            
            scaleX = (float(event.width) - 4) / float(width)
            scaleY = (float(event.height) - 4) / float(height)
            
            for face in self.objects:
                canvas.scale(face, 0, 0, scaleX, scaleY)

    def clear_canvas(self, canvas):
        if self.objects:
             canvas.delete("all")
