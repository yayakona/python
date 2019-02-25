# coding: UTF-8

def get_type_name(obj):
    return str(type(obj)).split('\'')[1]

if __name__ == '__main__':
    print(get_type_name(1))