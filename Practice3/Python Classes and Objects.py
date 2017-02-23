class Empdetail:
    #reate constructor
    def __init__(const1,empid,empname,empsal):
        const1.empid=empid
        const1.empname=empname
        const1.empsal=empsal
    #define display fx
    def dispdetails(const1):
        print("Employee ID: ",const1.empid)
        print("Employee Name: ",const1.empname)
        print("Employee Salary: ",const1.empsal)
'''
#object
obj1=Empdetail(101,"python",112333)
obj1.dispdetails()
'''

# inheretance in python
class Empaddress(Empdetail):
    def __init__(constchild,add,flat,state,empid,empname,empsal):
        constchild.add=add
        constchild.flat=flat
        constchild.state=state
        super(Empaddress,constchild).__init__(empid,empname,empsal)

    def dispadd(constchild):
        print("Employee add: ",constchild.add)
        print("Employee Flant Nukber: ",constchild.flat)
        print("Employee State: ",constchild.state)
        


childobj=Empaddress(721,"Apt1","NJ",16,"MantejS",323213)
childobj.dispdetails()
childobj.dispadd()
