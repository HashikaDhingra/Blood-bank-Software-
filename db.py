import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="bloodbank"
)
cursor = conn.cursor();
def insertProject(data):
    try:
        cursor.execute("insert into addpatients (PatientName,PatientPhoneNo,PatientAddress,PatientIssue,PatientDob,PatientGender,PatientBloodGroup) values (%s,%s,%s,%s,%s,%s,%s)",data)
        conn.commit();
        return True;
    except Exception as e:
        print(e)
        return False;

def showProject():
    try:
       cursor = conn.cursor(dictionary=True)
       cursor.execute("select * from addpatients");
       return (cursor.fetchall());
    except Exception as e:
        print("Issue in Selection ",e)
        return  False
    
def fetchdetailsbybloodgroup(data):
    try:
        print(data);
        q = "select * from addpatients where PatientBloodGroup='"+data+"'";
        print(q)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(q);
        return (cursor.fetchall());
    except Exception as e:
      print("Issue occur",e)
      return  False

def deletePatientsviaName(data):
    try:
        q = "delete from addpatients where PatientName='" + data + "'"
        cursor.execute(q);
        conn.commit()
        return True;

    except Exception as e:
        print(e)
        return False 
    

         
    
def donorProject(data):
    try:
        cursor.execute("insert into adddonors (dname,dphone,daddress,dmed,ddob,dgen,dblood) values (%s,%s,%s,%s,%s,%s,%s)",data)
        conn.commit();
        return True;
    except Exception as e:
        print(e)
        return False;

def showdonorDetail():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from adddonors");
        return (cursor.fetchall());
    except Exception as e:
      print("Issue in Selection ",e)
      return  False 

def deletedonorsviaName(data):
    try:
        q = "delete from adddonors where dname='" + data + "'"
        cursor.execute(q);
        conn.commit()
        return True;

    except Exception as e:
        print(e)
        return False 

def selectbyPatientName(data):
    try:
        cursor = conn.cursor(dictionary=True)
        q = "select * from addpatients where PatientName='"+data+"'"
        cursor.execute(q);
        return cursor.fetchall();

    except Exception as e:
        print(e)
        return []
    
def showbloodstock():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from blood_stocks");
        return (cursor.fetchall());
    except Exception as e:
      print("Issue in Selection ",e)
      return  False
    
def showbloodgroup():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from blood_stocks");
        return (cursor.fetchall());
    except Exception as e:
      print("Issue in Selection ",e)
      return  False

def selectbybloodgroup(data):
    try:
        cursor = conn.cursor(dictionary=True)
        q = "select * from blood_stocks where bgroup='"+data+"'"
        cursor.execute(q);
        return cursor.fetchall();

    except Exception as e:
        print(e)
        return []

def selectbyDonorName(data):
    try:
        cursor = conn.cursor(dictionary=True)
        q = "select * from adddonors where dname='"+data+"'"
        cursor.execute(q);
        return cursor.fetchall();

    except Exception as e:
        print(e)
        return []

    

    
def managestock(data):
    try:
        cursor.execute("insert into managestock (PatientName,bloodGroup,issueDate,IssueTime) values (%s,%s,%s,%s)",data)
        conn.commit();
        return True;
    except Exception as e:
        print(e)
        return False; 

def showqty(comQty):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select qty from blood_stocks where bgroup='"+comQty+"'");
        return (cursor.fetchall());
    except Exception as e:
       print("Issue in Selection ",e)
       return  False
    

def updateQty(comGrp,Qty):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE blood_stocks SET qty = %s WHERE bgroup = %s", (Qty, comGrp))
        conn.commit()
    except Exception as e:
      print("Issue in Selection ",e)


        
        