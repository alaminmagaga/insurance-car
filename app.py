import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('insurance.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict',methods=['POST'])
def predict():
    mac=request.form['months_as_customer']
    mac=int(mac)
    
    age=request.form['age']
    age=int(age)
    
    ps=request.form['policy_state']
    if ps =="OH":
        ps= 0
    elif ps == "IL":
        ps = 1
    elif ps == "IN":
        ps = 2
        
    pcl=request.form['policy_csl']
    if pcl =="250/500":
        pcl = 0
    elif pcl == "100/300":
        pcl = 1
    elif pcl == "500/1000":
        pcl = 2
       
    pd=request.form['policy_deductable']
    pd=int(pd)
    
    pap=request.form['policy_annual_premium']
    pap=int(pap)
    
    ul=request.form['umbrella_limit']
    ul=int(ul)
    
    iss=request.form['insured_sex']
    if iss =="female":
        iss= 0
    elif iss == "male":
        iss = 1
    
    iel=request.form['insured_education_level']
    if iel =="JD":
        iel= 0
    elif iel == "High School":
        iel = 1
    elif iel == "High School":
        iel = 2
    elif iel == "Associate":
        iel = 3
    elif iel == "MD":
        iel = 4
    elif iel == "PhD":
        iel = 5
    elif iel == "College":
        iel = 6
      
    io=request.form['insured_occupation']
    if io =="machine-op-inspct":
        io= 0
    elif io == "prof-specialty":
        io = 1
    elif io == "tech-support":
        io = 2
    elif io == "sales":
        io = 3
    elif io == "exec-managerial":
        io = 4
    elif io == "craft-repair":
        io = 5
    elif io == "transport-moving":
        io = 6
    elif io == "other-service":
        io = 7
    elif io == "priv-house-serv":
        io = 8
    elif io == "armed-forces":
        io = 9
    elif io == "adm-clerical":
        io = 10
    elif io == "protective-serv":
        io = 11
    elif io == "handlers-cleaners":
        io = 12
    elif io == "farming-fishing":
        io = 13
     
    ih=request.form['insured_hobbies']
    if ih =="reading":
        ih= 0
    elif ih == "paintball":
        ih = 1
    elif ih == "exercise":
        ih = 2
    elif ih == "movies":
        ih = 3
    elif ih == "golf":
        ih = 4
    elif ih == "camping":
        ih = 5
    elif ih == "kayaking":
        ih = 6
    elif ih == "yachting":
        ih = 7
    elif ih == "hiking":
        ih = 8
    elif ih == "video-games":
        ih = 9
    elif ih == "base-jumping":
        ih = 10
    elif ih == "skydiving":
        ih = 11
    elif ih == "board-games":
        ih = 12
    elif ih == "polo":
        ih = 13
    elif ih == "chess":
        ih = 14
    elif ih == "dancing":
        ih = 15
    elif ih == "sleeping":
        ih = 16
    elif ih == "cross-fit":
        ih = 17
    elif ih == "basketball":
        ih = 18
     
        
    ir=request.form['insured_relationship']
    if ir =="own-child":
        ir= 0
    elif ir == "other-relative":
        ir = 1
    elif ir == "not-in-family":
        ir = 2
    elif ir == "husband":
        ir = 3
    elif ir == "wife":
        ir = 4
    elif ir == "unmarried":
        ir = 5
   
    cg=request.form['capital-gains']
    cg=int(pd)
    
    cl=request.form['capital-loss']
    cl=int(cl)
    

    it=request.form['incident_type']
    if it =="Multi-vehicle Collision":
        it = 0
    elif it == "Single Vehicle Collision":
        it =1
    elif it == "Vehicle Theft":
        it =2
    elif it == "Parked Car":
        it =3
        
    
    ct=request.form['collision_type']
    if ct =="Rear Collision":
        ct = 0
    elif ct == "Side Collision":
        ct =1
    elif ct == "Front Collision":
        ct =2
        
        
    
        
        
    
    ins=request.form['incident_severity']
    if ins =="Minor Damage":
        ins = 0
    elif ins == "Total Loss":
        ins =1
    elif ins == "Major Damage":
        ins =2
    elif ins == "Trivial Damage":
        ins =3
        
    inc=request.form['incident_state']
    if inc =="NY":
        inc = 0
    elif inc == "WV":
        inc =1
    elif inc == "NC":
        inc =2
    elif inc == "VA":
        inc =3
    elif inc == "PA":
        inc =4
    elif inc == "OH ":
        inc =5
        
    ic=request.form['incident_city']
    if ic =="Springfield":
        ic = 0
    elif ic == "Arlington":
        ic =1
    elif ic == "Columbus":
        ic =2
    elif ic == "Northbend":
        ic =3
    elif ic == "Hillsdale":
        ic =4
    elif ic == "Riverwood":
        ic =5
    elif ic == "Northbrook":
        ic =6
        
    inl=request.form['incident_location']
    if inl =="1532 Washington St":
        inl = 0
    elif inl == "3872 5th Drive":
        inl =1
    elif inl == "9821 Francis Ave":
        inl =2
    elif inl == "others":
        inl =3
        
    iod=request.form['incident_hour_of_the_day']
    iod=int(iod)
    
    nvi=request.form['number_of_vehicles_involved']
    nvi=int(nvi)
        
    prd=request.form['property_damage']
    if prd =="No":
        prd = 0
    elif prd == "Yes":
        prd =1

    bi=request.form['bodily_injuries']
    bi=int(bi)
  
    wt=request.form['witnesses']
    wt=int(wt)
    
    pra=request.form['police_report_available']
    if pra =="No":
        pra = 0
    elif pra == "Yes":
        pra =1
   
    
    tca=request.form['total_claim_amount']
    tca=int(tca)
    
    ic=request.form['injury_claim']
    ic=int(ic)
    
    pc=request.form['property_claim']
    pc=int(pc)
    
    vc=request.form['vehicle_claim']
    vc=int(vc)
    
    ay=request.form['auto_year']
    ay=int(ay)
    
    pby=request.form['policy_bind_year']
    pby=int(pby)
    
    pbm=request.form['policy_bind_month']
    pbm=int(pbm)
    
    pbd=request.form['policy_bind_day']
    pbd=int(pbd)
    
    
    
    
    
    
   
    int_features = [mac,age,ps,pcl,pd,pap,ul,iss,iel,io,ih,ir,cg,cl,it,ct,ins,inc,ic,inl,iod,nvi,prd,bi,wt,pra,tca,ic,pc,vc,ay,pby,pbm,pbd]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    

    return render_template('result.html', prediction_text='The Passenger {}'.format(prediction[0]),prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
    
    
