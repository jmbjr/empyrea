import os, random, re

def MakeLang(langfile = None,MINLEN = 3,MAXLEN = 9,caphy = True):
    langdict = {}
    startpairs = []
    starttrios = []
    endpairs = []
    keydict = {}

    langdict['caphy'] = caphy

    namedir = '.\\data\\name'
    if not langfile:        
        langdir = os.listdir(namedir)
        langdir.remove('verboten.txt')
        filedir = namedir + '\\' + random.choice(langdir)
    else:
        filedir = namedir + '\\' + langfile + '.txt'

    langfile = open(filedir, 'r')
    namelist = map(lambda x: x.strip('\n'), langfile.readlines())
    langfile.close()

    for name in namelist:

        name = name.lower()
        pair = name[:2]
        trio = name[:3]
        endpair = name[-2:]
        startpairs.append(pair)
        starttrios.append(trio)
        endpairs.append(endpair)

        for l in range(len(name)):
            if l > 2:
                if keydict.get(name[l -3:l]):
                    keydict[name[l - 3:l]] += name[l]
                else:
                    keydict[name[l - 3:l]] = name[l]
            if l < len(name) - 1:
                if keydict.get(name[l]):
                    keydict[name[l]] += name[l + 1]
                else:
                    keydict[name[l]] = name[l + 1]
            if l < len(name) - 2:
                if keydict.get(name[l:l+2]):
                    keydict[name[l:l+2]] += name[l + 2]
                else:
                    keydict[name[l:l+2]] = name[l + 2]

    langdict['keydict'] = keydict
    langdict['startpairs'] = startpairs
    langdict['starttrios'] = starttrios
    langdict['endpairs'] = endpairs
    langdict['MINLEN'] = MINLEN
    langdict['MAXLEN'] = MAXLEN

    return langdict

def MakeName(langdict):

    conlist = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    vowlist = ['a','e','i','o','u','y']
    
    while True:
        startpair = random.choice(langdict['startpairs']).capitalize()
        name = startpair
        for l in range(random.randrange(langdict['MINLEN'],langdict['MAXLEN'] + 1) - 2):
            try:
                curpair = name[-2:]
                name += random.choice(list(langdict['keydict'][curpair]))
            except KeyError:
                try:
                    name += random.choice(list(langdict['keydict'][name[-1]]))
                except KeyError:
                    break

        killswitch = False

        for l in range(len(name)):
            if l > 1:
                if name[l] in conlist and name[l - 1] in conlist and name[l - 2].lower() in conlist:
                    if not langdict['keydict'].get(name[l - 2].lower() + name[l - 1] + name[l]):
                        killswitch = True
                elif name[l] in vowlist and name[l - 1] in vowlist and name[l - 2].lower() in vowlist:
                    if not langdict['keydict'].get(name[l - 2].lower() + name[l - 1] + name[l]):
                        killswitch = True

        if name[0].lower() in conlist and name[1] in conlist and name[2] in conlist:
            if not name[:3] in langdict['starttrios']:
                killswitch = True

        if killswitch:
            continue

        if langdict['caphy']:
            name = list(name)
            for letter in range(len(name)):
                if name[letter] == '-':
                    name[min(letter + 1,len(name) - 1)] = name[min(letter + 1,len(name) - 1)].upper()
            name = ''.join(name)

        if re.search('[aeiou]{3}',name):
            continue

        if name[-2:] not in langdict['endpairs']:
            continue

        if len(name) > langdict['MINLEN']:
            break
                
    return name
