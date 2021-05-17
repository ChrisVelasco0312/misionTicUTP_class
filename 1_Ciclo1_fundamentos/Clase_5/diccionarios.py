dev = {
    'salary' : 1500000,
    'name': 'Christian',
    'skills':{
        'lenguajes': { 
            1 : 'Python',
            2: 'Java',
            3: 'JavaScript',
            4: 'Haskell',
            5: 'C++'
        },
        'entorno': 'VScode'
    },
    'experience': {
        'jr' : 2,
        'pro' : 3,
        'senior': 4,
        'DBA': 2
    }
}

print(dev['salary'])
print(dev['name'])

## Acceso a diccionarios dentro de diccionarios
print(dev['skills']['lenguajes'])
print(dev['skills']['entorno'])

## Calcular el total de años de experiencia
def calc_total_exp():
    total_exp = dev['experience']['jr'] + \
                dev['experience']['pro'] + \
                dev['experience']['senior'] + \
                dev['experience']['DBA']
    print(total_exp)

calc_total_exp()

print(dev['skills']['lenguajes'][2])
