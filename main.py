
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

usuarios =[]

id_contador =1


@app.route("/", methods=["GET","POST"])
def crud():
    global id_contador

    if request.method=="POST": #si accedemos a la ruta con datos en el formulario
        nombre = request.form.get("nombre")
        email = request.form.get("email") 
        usuarios.append({"id":id_contador,"username":nombre,"email":email})#insertando usuario
        id_contador+=1
        return redirect(url_for("crud"))

    id_eliminar=request.args.get("borrar") #siempre queda como texto
    if id_eliminar:  #si me entregan una id a eliminar
        #TODO: Eliminar el usuario con el id del parametro de la lista
        for item in usuarios:
            if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for("crud"))  #llamar al nombre de la funcion
    


    return render_template("registro.html", usuarios=usuarios) #lista que entregamos al html
    
    
#ruta de actualizacion de los datos del usuario

@app.route("/update/<int:id>", methods=["GET","POST"]) #ruta con parametros
def update(id):
    
    estudiante_a_editar=""
    

    #TODO: identificar el diccionario del usuario con id a entregar
    for diccionario in usuarios:
        if diccionario["id"]==id:
            estudiante_a_editar=diccionario
            print("El estudiante a editar es",estudiante_a_editar)
            break
    if request.method=="POST":
        #TODO:actualizar el diccionario del estudiante con los datos del formulario
        estudiante_a_editar("username")=request.form.get("nombre")
        estudiante_a_editar("email")=request.form.get("email")
        return redirect(url_for("crud"))
    
    #si despuies de recorrer toda la lista, no encontramos el id entregado
    if estudiante_a_editar=="":
        return f"no existe el usuario con id:{id}" #salgo de la funcion

    return render_template("editar.html",estudiante_a_editar=estudiante_a_editar)

if __name__ == "_main_":
    app.run(debug=True)

