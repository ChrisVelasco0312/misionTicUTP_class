## Cada año como jr 200000, como pro 300000,
## como senior 500000, como DBA 500000

dev = {
    'salary' : 1500000,
    'name': 'Christian',
    'skills':{
        'lenguajes': { 
            1 : 'Python',
            2: 'Java',
            3: 'JavaScript',
            4: 'Haskell',
            5: 'C++',
        },
        'entorno': 'VScode',
    },
    'experience': {
        'jr' : 2,
        'pro' : 3,
        'senior': 4,
        'DBA': 2
    }
}

def experience_bonus(dev):
    jr = 200000 * dev['experience']['jr']
    pro = 300000 * dev['experience']['pro']
    senior =  500000 * dev['experience']['senior']
    DBA = 500000 * dev['experience']['DBA']

    total_bonus = jr + pro + senior + DBA

    dev['salary'] += total_bonus
    return dev['salary']

print(experience_bonus(dev))




