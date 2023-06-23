from flask import Flask,render_template,request,session
import uuid    #generates unique key
import os
import schedule

app = Flask(__name__)
app.secret_key="SecretKey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/designSelection")
def designSelection():
    return render_template('designSelection.html')

@app.route("/form/<string:design>", methods=["GET","POST"])
def form(design):
    session['design_sess']=design
    return render_template('form.html')

@app.route("/upload", methods=["GET","POST"])
def upload():
    design_upload=session.get("design_sess")
    if design_upload=='design1':
        design_name='Design1.html'
    elif design_upload=='design2':
        design_name='Design2.html'
    elif design_upload=='design3':
        design_name='Design3.html'
    elif design_upload=='design4':
        design_name='Design4.html'

    if request.method=='POST':
        firstname = request.form.get('firstname')
        lastname =request.form.get('lastname')
        shortdesc=request.form.get('shortdesc')
        schoolname =request.form.get('schoolname')
        collegename =request.form.get('collegename')
        phoneno =request.form.get('phoneno')
        email =request.form.get('email')
        skill1 =request.form.get('skill1')
        skill2 =request.form.get('skill2')
        skill3 =request.form.get('skill3')
        skill4 =request.form.get('skill4')
        skill5 =request.form.get('skill5')
        about =request.form.get('about')
        github=request.form.get('github')
        linkedin=request.form.get('linkedin')
        project11=request.form.get('project11')
        project12=request.form.get('project12')
        project13=request.form.get('project13')

        project21=request.form.get('project21')
        project22=request.form.get('project22')
        project23=request.form.get('project23')

        project31=request.form.get('project31')
        project32=request.form.get('project32')
        project33=request.form.get('project33')

        project41=request.form.get('project41')
        project42=request.form.get('project42')
        project43=request.form.get('project43')

        


        #image uploading (single)
        profilepic=request.files["profilepic"]
        profilepic.save(f'static/images/{profilepic.filename}')
        

        key=uuid.uuid1()
        profilepic_new_name=f"{key}{profilepic.filename}"
        os.rename(f'static/images/{profilepic.filename}',f'static/images/{profilepic_new_name}')   #to avoid replication

        # print(firstname)
        # print(lastname )
        # print(schoolname )
        # print(collegename )
        # print(phoneno )
        # print(email )
        # print(skill1 )
        # print(skill2)
        # print(skill3 )
        # print(skill4 )
        # print(skill5 )
        # print(shortdesc )

    # return "uploaded"
    return render_template(design_name,dname=firstname,dlname=lastname,dshortdesc=shortdesc,dabout=about,ds1=skill1,ds2=skill2,ds3=skill3,ds4=skill4,ds5=skill5,profilepic=profilepic_new_name,dgithub=github,dlinkedin=linkedin,dschoolname=schoolname,dcollegename=collegename,demail=email,dphone=phoneno,dproject11=project11,dproject12=project12,dproject13=project13, dproject21=project21,dproject22=project22,dproject23=project23, dproject31=project31,dproject32=project32,dproject33=project33,dproject41=project41,dproject42=project42,dproject43=project43)

def delete():
    files=os.listdir("static\images")
    for i in files:
        os.remove(f"static/images/{i}")
        # print(i)


if __name__=="__main__":
    schedule.every().day.at("23:59").do(delete)
    app.run(debug=True)