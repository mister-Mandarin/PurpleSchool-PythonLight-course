role: str = 'admin'

match role:
    case 'admin':
        print('asdf')
    case _: pass
