# Deckert, Timothy
# 1000-637-406
# 2017-09-01
# Assignment_00_03

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

        if self.objects:
             canvas.delete("all")
	
        rows = data.splitlines()

        vertices = []
        faces = []

        for row in rows:

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

##        print(dxy)
##        print(sxy)
##        print(dvpxy)

        transform = np.dot(dvpxy, np.dot(sxy,dxy))
##        print (transform)

        particles = []

        for vertex in vertices:
            particles.append(np.dot(transform, vertex))
##            print (vertex)

        points = []

        for face in faces:
            for fp in face:
                points.append(int(particles[int(fp)-1][0]))
                points.append(int(particles[int(fp)-1][1]))
        
            self.objects.append(canvas.create_polygon(points, outline="red", fill="yellow"))
            points = []
##        print (points)
##        print (faces)
##        print (window)
##        print (viewport)
        #print (canvas.cget("width"))
        #print (canvas.cget("height"))

    def redisplay(self, canvas, event):
        if self.objects:
            #for index, face in enumerate(self.objects):
             #   if index == 0:
                    
              #  print (canvas.coords(face))
            canvas.coords(self.objects[0], 0, 0, event.width, event.height)
            canvas.coords(self.objects[1], event.width, 0, 0, event.height)
            canvas.coords(self.objects[2], int(0.25 * int(event.width)),
                          int(0.25 * int(event.height)),
                          int(0.75 * int(event.width)),
                          int(0.75 * int(event.height)))
