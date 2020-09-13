from Mysqsl_module import con

def checkId(*args) -> str:
    con.cursor.execute(f"select Name_user from Users where Id_user={args[0]}")
    result=con.cursor.fetchone()

    return result[0]

def checkPassw(*args) -> bool:
    print(args[0],args[1])

    con.cursor.execute(f"select COUNT(*) from Users where Id_user='{args[0]}' and Clave_user='{args[1]}'")
    result = con.cursor.fetchone()

    return result[0]==1

keys_functions = {
    'check-id': checkId,
    'check-pass': checkPassw
}
