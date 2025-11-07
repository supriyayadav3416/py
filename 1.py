def main():
    int_var = 7
    float_var = 5.3
    str_var = "welcome"
    list_var = [1,2,3]
    tpl_var = (4,5,6)
    dict_var = {"name":"lucy" , "age":"34"}
    set_var = {4,5,6}
    bool_var = False

#printing all
    print("initial values")
    print(f"integer:{int_var}")
    print(f"float:{float_var}")
    print(f"string:{str_var}")
    print(f"list:{list_var}")
    print(f"tuple:{tpl_var}")
    print(f"dictionary:{dict_var}")
    print(f"set:{set_var}")
    print(f"boolean:{bool_var}")
    print("-"*50)   

#numeric operations
    sum_num = int_var + float_var
    power_num = int_var ** 2
    print("numeric operations")
    print(f"sum = {sum_num}") 
    print(f"power = power_num") 
    print("-"*50)   

#string operations
    new_str = str_var = "to recoe"
    sub_str = new_str[4:10]
    print("string operations") 
    print(f"new string = {new_str}")
    print(f"sub string = {sub_str}")
    print("-"*50) 

#boolean operations
    and_res = bool_var and False
    or_res = bool_var or True
    not_res = not bool_var 
    print("boolean operations")
    
    print(f"and = {and_res}")  
    print(f"or = {or_res}")  
    print(f"not = {not_res}")        
    
    
if __name__=='__main__' :
    main()



