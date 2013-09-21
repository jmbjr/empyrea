#############################################################################
#                                                                           #
#  Language Naming Scheme Generator                                         #
#  Written in Python by David M. Hagar                                      #
#  January, 2010                                                            #
#                                                                           #
#  Permission to use, copy, modify, and distribute this software for any    #
#  purpose without fee is hereby granted, provided that this entire notice  #
#  is included in all copies of any software which is or includes a copy    #
#  or modification of this software and in all copies of the supporting     #
#  documentation for such software.                                         #
#  THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED  #
#  WARRANTY. IN PARTICULAR, THE AUTHOR DOES NOT MAKE ANY                    #
#  REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY    #
#  OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.              #
#                                                                           #
#############################################################################

import random
import math

__author__ = 'D.M. Hagar'
__version__ = '0.1 Language Naming Scheme Generator by ' + __author__

####################################
# Flag initialization.             #
####################################

langUsesCC = False
langUsesVC = False
langOnlyVStart = False
langOnlyCStart = False
langOnlyVEnd = False
langOnlyCEnd = False
langCCStart = False
langCCMid = False
langCCEnd = False
langVCStart = False
langVCMid = False
langVCEnd = False
langHSPerc = 50
langCCPerc = 50
langVCPerc = 50

####################################
# Letter and letter cluster lists. #
####################################

# Letter Weighting List
lwlist = {'a':9, 'b':2, 'c':5, 'd':3, 'e': 11, 'f':2, 'g':2, \
       'h':3, 'i':8, 'j':1, 'k':2, 'l':5, 'm':3, 'n':7, 'o':7, \
       'p':3, 'q':1, 'r':8, 's':6, 't':7, 'u':4, 'v':2, 'w':1, \
       'x':1, 'y':2, 'z':1}

# Vowels
vlist = ['a', 'e', 'i', 'o', 'u']

# Vowel clusters

vcclist = ['ae', 'ai', 'ao', 'au', 'ay', 'aw', \
           'ea', 'ee', 'ei', 'eo', 'ey', 'ia', \
           'ie', 'io', 'oa', 'oe', 'oi', 'oo', \
           'ou', 'ua']

vculist = ['aa', 'eu', 'ew', 'iu', 'iy', 'ii', \
           'oy', 'ow', 'ue', 'ui', 'uo', 'uy']

# Consonants
nclist = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', \
 'n', 'p', 'r', 's', 't', 'y']

uclist = ['q','v','w','x','z']

# Consonant clusters, common

ccclist = ['br', 'bl', 'cr', 'cl', 'dr', 'dw', 'fl', 'fr', 'gr', 'gl', 'kl', \
 'kr', 'pr', 'pl', 'st', 'sw', 'sl', 'tr']

# Consonant clusters, uncommon
cculist = ['bh', 'ch', 'dh', 'fh', 'gh', 'jh', 'kh', 'lh', 'ph', \
 'rh', 'sh', 'th', 'vh', 'wh', 'xh', 'yh', 'zh', 'wr', \
 'sv', 'spl', 'str', 'sch', 'cz', 'cw', 'fj', 'fhr']

# Consonant clusters, repeated
ccrlist = ['cc', 'dd', 'ff', 'gg', 'kk', 'll', 'mm', 'nn', 'pp', \
           'rr', 'ss', 'tt', 'vv', 'ww', 'xx', 'yy', 'zz']

# Consonant clusters, rare soft

ccrslist = ['bw', 'bz', 'bv', 'bs', 'by', 'bsh', 'bth', 'bx', 'bj', 'bf', \
 'cv', 'cs', 'cy', 'csh', 'cth', 'cx', 'cj', 'cf', \
 'dy', 'dv', 'dl' 'ds', 'dz', 'dsh', 'dth', 'dx', 'dj', 'df', \
 'fw', 'fz', 'fy', 'fv', 'fs', 'fsh', 'fth', 'fx', \
 'gw', 'gz', 'gy', 'gv', 'gs', 'gsh', 'gth', 'gx', 'gj', 'gf', \
 'kw', 'kz', 'ky', 'kv', 'ks', 'ksh', 'kth', 'kx', 'kj', 'kf', \
 'hw', 'hz', 'hy', 'hl', 'hv', 'hs', 'hth', 'hx', 'hj', 'hf', \
 'jw', 'jz', 'jy', 'jv', 'jl', 'js', 'jth', 'jx', 'jf', \
 'lw', 'lz', 'ly', 'lv', 'ls', 'll', 'lth', 'lx', 'lj', 'lf', 'lsh', \
 'mw', 'mz', 'my', 'mv', 'ms', 'ml', 'mth', 'mx', 'mj', 'mf', 'msh', \
 'nw', 'nz', 'ny', 'nv', 'ns', 'nl', 'nth', 'nx', 'nj', 'nf', 'nsh', \
 'pw', 'pz', 'py', 'pv', 'ps', 'pth', 'px', 'pj', 'pf', 'psh', \
 'qu', 'qw', 'qz', 'qy', 'qv', 'ql', 'qs', 'qth', 'qx', 'qj', 'qf', 'qsh', \
 'rw', 'rz', 'ry', 'rv', 'rs', 'rl', 'rth', 'rx', 'rj', 'rf', \
 'sz', 'sy', 'ss', 'sth', 'sx', 'sj', 'sf', \
 'tw', 'tz', 'ty', 'tv', 'ts', 'tl', 'tx', 'tj', 'tf', \
 'vw', 'vz', 'vy', 'vs', 'vth', 'vx', 'vl', 'vj', 'vf', \
 'wz', 'wy', 'wv', 'ws', 'wth', 'wx', 'wj', 'wl', 'wf', \
 'xw', 'xz', 'xy', 'xv', 'xs' 'xj', 'xf', 'xth', 'xl', \
 'yw', 'yz', 'ys', 'yth', 'yx', 'yl', 'yj', 'yf', 'yj',
 'zw', 'zy', 'zv', 'zs', 'zl', 'zth', 'zx', 'zj', 'zf']

# Consonant clusters, rare hard

ccrhlist = ['bd', 'bg', 'bk', 'bm', 'bn', 'bp', 'bt', \
 'db', 'dg', 'dk', 'dm', 'dn', 'dp', 'dt', \
 'gb', 'gd', 'gk', 'gm', 'gn', 'gp', 'gt', \
 'kb', 'kd', 'kg', 'km', 'kn', 'km', 'kp', 'kt', \
 'mb', 'md', 'mg', 'mk', 'mn', 'mp', 'mr', 'mt', \
 'nb', 'nd', 'ng', 'nk', 'np', 'nm', 'nr', 'nt', \
 'pb', 'pd', 'pg', 'pk', 'pm', 'pn', 'pr', 'pt', \
 'rb', 'rd', 'rg', 'rk', 'rm', 'rn', 'rp', 'rt', \
 'tb', 'td', 'tg', 'tk', 'tm', 'tn', 'tp']

# Consonant clusters, ending-appropriate

ccelist = ['ys', 'yth', 'yx', 'yl', 'ws', 'wth', 'wy', 'ty', 'ry', \
 'nth', 'ms', 'ly', 'ls', 'll', 'lth', 'ds', 'dy', 'gy', 'fy', \
 'my', 'ny', 'py', 'sy', 'vy', 'zy', 'cs', 'by', 'ss', 'st', \
 'ch', 'dh', 'kh', 'sh', 'th', 'mz', 'ns']

####################################
# Basic Language Prefs             #
####################################

def MakeLang(langNormPerc=False):
    """Builds a language dictionary.

    Takes optional configuration parameters, returns the dictionary."""
    
    global langUsesCC, langUsesVC, langOnlyVStart, langOnlyCStart, \
           langOnlyVEnd, langOnlyCEnd, langCCStart, langCCMid, \
           langCCEnd, langVCStart, langVCMid, langVCEnd, langHSPerc, \
           langCCPerc, langVCPerc

    langdict = {}
    
    # Does the language use consonant clusters?
    if random.randrange(1,11) == 1:
        langUsesCC = False
    else:
        langUsesCC = True
        # How often will clusters replace single consonants if applicable?
        # (Least [1] <---> [100] Most)
        langCCPerc = random.randrange(25,65)
    # Does the language use vowel clusters?
    if random.randrange(1,11) == 1:
        langUsesVC = False
    else:
        langUsesVC = True
        # How often will clusters replace single vowels if applicable?
        # (Least [1] <---> [100] Most)
        langVCPerc = random.randrange(10,35)

    # On a scale of 1-10 (Most [1] <---> [10] Least), how 'normal'-sounding
    # (i.e. uses consonant clusters similar to English) will our language be?
    if not langNormPerc:
        langNormPerc = random.randrange(1,4)
    # What is the acceptable range of syllable components in a name?
    # (Keep in mind a component is either a nucleus or coda, not a
    # whole syllable.)
    lengthMin = random.randrange(3,6)
    lengthMax = random.randrange(lengthMin + 2,8)

####################################
# Name Start/End Preferences       #
####################################

    # Will the language only permit names starting with vowels?
    if random.randrange(1,11) == 1:
        langOnlyVStart = True
    else:
        langOnlyVStart = False
        # If not, will it only permit names starting with consonants?
        if random.randrange(1,11) == 1:
            langOnlyCStart = True
        else:
            langOnlyCStart = False

    # Will the language only permit names ending with vowels?
    if random.randrange(1,11) == 1:
        langOnlyVEnd = True
    else:
        langOnlyVEnd = False
        # If not, will it only permit names ending with consonants?
        if random.randrange(1,11) == 1:
            langOnlyCEnd = True
        else:
            langOnlyCEnd = False

####################################
# Cluster configuration.           #
####################################

    # Does the language use c. clusters for the beginning of names?
    if random.randrange(1,5) > 1 and langUsesCC:
        langCCStart = True
    else:
        langCCStart = False
    # Does the language use c. clusters in the middle of names?
    if random.randrange(1,5) > 1 and langUsesCC:
        langCCMid = True
    else:
        langCCMid = False
    # Does the language use c. clusters at the end of names?
    if random.randrange(1,5) > 1 and langUsesCC:
        langCCEnd = True
    else:
        langCCEnd = False
    # Does the language use v. clusters for the beginning of names?
    if random.randrange(1,5) > 1 and langUsesVC:
        langVCStart = True
    else:
        langVCStart = False
    # Does the language use v. clusters in the middle of names?
    if random.randrange(1,5) > 1 and langUsesVC:
        langVCMid = True
    else:
        langVCMid = False
    # Does the language use v. clusters at the end of names?
    if random.randrange(1,5) > 1 and langUsesVC:
        langVCEnd = True
    else:
        langVCEnd = False
    # Does the language use rare soft c. clusters?
    if random.randrange(1,6) == 1 and langUsesCC:
        langRSCC = True
    else:
        langRSCC = False
    # Does the language use rare hard c. clusters?
    if random.randrange(1,6) == 1 and langUsesCC:
        langRHCC = True
    else:
        langRHCC = False
    # Does the language use repeated consonants?
    if random.randrange(1,3) == 1:
        langRC = True
    else:
        langRC = False

    # We'll now be weighting specific random consonants
    # and vowels to see which ones our language uses the most.

    vweightlist = []
    cweightlist = []
    vcweightlist = []
    ccweightlist = []
    cceweightlist = []

    for vowel in vlist:
        vweightlist.extend([vowel] * random.randrange(1,5) * lwlist[vowel])
            
    for consonant in nclist + uclist:
        cweightlist.extend([consonant] * random.randrange(1,5) * lwlist[consonant])

    # If we're using clusters, now it's time to weight them, too.

    if langUsesVC:

        for cluster in vcclist:
            clusterweight = 0
            for letter in list(cluster):
                clusterweight += lwlist[letter]
            clusterweight = int(clusterweight / 3)
            vcweightlist.extend([cluster] * clusterweight * (vweightlist.count(list(cluster)[0]) + vweightlist.count(list(cluster)[1]) + random.randrange(1,6)))

        for cluster in vculist:
            clusterweight = 0
            for letter in list(cluster):
                clusterweight += lwlist[letter]
            clusterweight = int(clusterweight / 3)
            vcweightlist.extend([cluster] * int(clusterweight * .5))

        flist = []
        for cluster in range(5,10):
            flist.append(random.choice(vcweightlist))
        vcweightlist = flist

    if langUsesCC:
        for cluster in ccclist:
            clusterweight = 0
            for letter in list(cluster):
                clusterweight += lwlist[letter]
            ccweightlist.extend([cluster] * clusterweight * ((10 - langNormPerc) * random.randrange(1,50)))

        for cluster in cculist:
            clusterweight = 0
            for letter in list(cluster):
                clusterweight += lwlist[letter]
            clusterweight = int(clusterweight / 5)
            ccweightlist.extend([cluster] * clusterweight * int((float(math.sqrt((3 - langNormPerc) * (3 - langNormPerc))) / 1.0) * 2 * random.randrange(1,25)))
        if langRC:
            for cluster in ccrlist:
                clusterweight = 0
                for letter in list(cluster):
                    clusterweight += lwlist[letter]
                clusterweight = int(clusterweight / 10)
                ccweightlist.extend([cluster] * clusterweight * ((langNormPerc) * random.randrange(1,15)))
        if langRSCC:
            for cluster in ccrslist:
                clusterweight = 0
                for letter in list(cluster):
                    clusterweight += lwlist[letter]
                clusterweight = int(clusterweight / 10)
                ccweightlist.extend([cluster] * clusterweight * (langNormPerc * ((100 - langHSPerc) / random.randrange(30,50))) * random.randrange(1,5))
        if langRHCC:
            for cluster in ccrhlist:
                clusterweight = 0
                for letter in list(cluster):
                    clusterweight += lwlist[letter]
                clusterweight = int(clusterweight / 10)
                ccweightlist.extend([cluster] * clusterweight * (langNormPerc * ((langHSPerc) / random.randrange(30,50))) * random.randrange(1,5))

        flist = []
        for cluster in range(5,15):
            flist.append(random.choice(ccweightlist))
        ccweightlist = flist

        if langCCEnd:
            for cluster in ccelist:
                clusterweight = 0
                for letter in list(cluster):
                    clusterweight += lwlist[letter]
                clusterweight = int(clusterweight / 3)
                cceweightlist.extend([cluster] * random.randrange(1,15))

            flist = []
            for cluster in range(5,15):
                flist.append(random.choice(cceweightlist))
            cceweightlist = flist

    # Add all of our language information to a dictionary to be exported from the module.

    langdict['langUsesCC'] = langUsesCC
    langdict['langUsesVC'] = langUsesVC
    langdict['langOnlyVStart'] = langOnlyVStart
    langdict['langOnlyVEnd'] = langOnlyVEnd
    langdict['langOnlyCStart'] = langOnlyCStart
    langdict['langOnlyCEnd'] = langOnlyCEnd
    langdict['langCCStart'] = langCCStart
    langdict['langCCMid'] = langCCMid
    langdict['langCCEnd'] = langCCEnd
    langdict['langVCStart'] = langVCStart
    langdict['langVCMid'] = langVCMid
    langdict['langVCEnd'] = langVCEnd
    langdict['langRSCC'] = langRSCC
    langdict['langRHCC'] = langRHCC
    langdict['langRC'] = langRC
    langdict['langHSPerc'] = langHSPerc
    langdict['langCCPerc'] = langCCPerc
    langdict['langVCPerc'] = langVCPerc
    langdict['vweightlist'] = vweightlist
    langdict['vcweightlist'] = vcweightlist
    langdict['cweightlist'] = cweightlist
    langdict['ccweightlist'] = ccweightlist
    langdict['cceweightlist'] = cceweightlist
    langdict['lengthMin'] = lengthMin
    langdict['lengthMax'] = lengthMax

    return langdict

####################################
# Name Generation                  #
####################################

def MakeName(langdict):
    """Generates a name based on the settings in a language dictionary.

    Requires the language dictionary to be passed as a parameter."""

    langUsesCC = langdict['langUsesCC']
    langUsesVC = langdict['langUsesVC']
    langOnlyVStart = langdict['langOnlyVStart']
    langOnlyVEnd = langdict['langOnlyVEnd']
    langOnlyCStart = langdict['langOnlyCStart']
    langOnlyCEnd = langdict['langOnlyCEnd']
    langCCStart = langdict['langCCStart']
    langCCMid = langdict['langCCMid']
    langCCEnd = langdict['langCCEnd']
    langVCStart = langdict['langVCStart']
    langVCMid = langdict['langVCMid']
    langVCEnd = langdict['langVCEnd']
    langHSPerc = langdict['langHSPerc']
    langCCPerc = langdict['langCCPerc']
    langVCPerc = langdict['langVCPerc']
    vweightlist = langdict['vweightlist']
    vcweightlist = langdict['vcweightlist']
    cweightlist = langdict['cweightlist']
    ccweightlist = langdict['ccweightlist']
    cceweightlist = langdict['cceweightlist']
    lengthMin = langdict['lengthMin']
    lengthMax = langdict['lengthMax']

    # How many components does our name have?

    takenclusters = []
    nameComps = random.randrange(lengthMin, lengthMax)
    nameCompStart = nameComps
    name = []

    # Will our starting component be a vowel/cluster or a consonant/cluster?
    if langOnlyVStart:
        curCompType = 'v'
    else:
        if langOnlyCStart:
            curCompType = 'c'
        else:
            if random.randrange(1,3) == 1:
                curCompType = 'v'
            else:
                curCompType = 'c'

    # The main loop of name generation.
    while nameComps > 0:
        # If it's a vowel component, determine whether it's a cluster or not.
        if curCompType == 'v':
            if langUsesVC:
                if random.randrange(1,151) < langVCPerc:
                    isCluster = True
                    if nameComps == nameCompStart:
                        if not langVCStart:
                            isCluster = False
                    elif nameComps == 1:
                        if not langVCEnd:
                            isCluster = False
                    else:
                        if not langVCMid:
                            isCluster = False
                else:
                    isCluster = False
            else:
                isCluster = False
        # Otherwise, if it's a consonant component, do the same.
        elif curCompType == 'c':
            if langUsesCC:
                if random.randrange(1,101) < langCCPerc:
                    isCluster = True
                    if nameComps == nameCompStart:
                        if not langCCStart:
                            isCluster = False
                    elif nameComps == 1:
                        if not langCCEnd:
                            isCluster = False
                    else:
                        if not langCCMid:
                            isCluster = False
                else:
                    isCluster = False
            else:
                isCluster = False
                
        # If we are only using vowel/consonant name end components,
        # trim down extra components if necessary.
        if curCompType == 'v' and nameComps == 2 and langOnlyVEnd:
            nameComps = 1
        elif curCompType == 'c' and nameComps == 2 and langOnlyCEnd:
            nameComps = 1

        # Now we just choose which weighted list to use.
        if curCompType == 'v':
            if isCluster:
                compList = vcweightlist
            else:
                compList = vweightlist
        else:
            if isCluster:
                if nameComps == 1:
                    compList = cceweightlist
                else:
                    compList = ccweightlist
            else:
                compList = cweightlist

        # Randomly select an element from the weighted list and add it to our name.
        try:
            selectedcomp = random.choice(compList)
            if len(selectedcomp) > 1:
                while True:
                    if selectedcomp not in takenclusters:
                        takenclusters.append(selectedcomp)
                        break
                    elif selectedcomp in takenclusters:
                        selectedcomp = random.choice(compList)
                        pass
                    
            name.append(selectedcomp)
        except IndexError:
            compList = vweightlist
            selectedcomp = random.choice(compList)
            if len(selectedcomp) > 1:
                while True:
                    if selectedcomp not in takenclusters:
                        takenclusters.append(selectedcomp)
                        break
                    elif selectedcomp in takenclusters:
                        selectedcomp = random.choice(compList)
                        pass
                    
            name.append(selectedcomp)
        
        # Reduce the number of components to go by one and change the component type.
        if curCompType == 'v':
            curCompType = 'c'
        else:
            curCompType = 'v'
        nameComps -= 1

    name = ''.join(name).capitalize()
    return name
    
