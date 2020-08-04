import dis

code = """flag=True; if flag:
            print('t')
       """

dis.dis(code)
