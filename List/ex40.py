# Write a Python program to split a list based on the first character of a word.

def split_first_char(li):
    a = ["a"]
    b = ["b"]
    c = ["c"]
    d = ["d"]
    e = ["e"]
    f = ["f"]
    g = ["g"]
    h = ["h"]
    i = ["i"]
    j = ["j"]
    k = ["k"]
    l = ["l"]
    m = ["m"]
    n = ["n"]
    o = ["o"]
    p = ["p"]
    q = ["q"]
    r = ["r"]
    s = ["s"]
    t = ["t"]
    u = ["u"]
    v = ["v"]
    w = ["w"]
    x = ["x"]
    y = ["y"]
    z = ["z"]
   
    for letter in li:
        if letter[0] == "a":
            a.append(letter)
        if letter[0] == "b":
            b.append(letter)
        if letter[0] == "c":
            c.append(letter)
        if letter[0] == "d":
            d.append(letter)
        if letter[0] == "e":
            e.append(letter)
        if letter[0] == "f":
            f.append(letter)
        if letter[0] == "g":
            g.append(letter)
        if letter[0] == "h":
            h.append(letter)
        if letter[0] == "i":
            i.append(letter)
        if letter[0] == "j":
            j.append(letter)
        if letter[0] == "k":
            k.append(letter)
        if letter[0] == "l":
            l.append(letter)
        if letter[0] == "m":
            m.append(letter)
        if letter[0] == "n":
            n.append(letter)
        if letter[0] == "o":
            o.append(letter)
        if letter[0] == "p":
            p.append(letter)
        if letter[0] == "q":
            q.append(letter)
        if letter[0] == "r":
            r.append(letter) 
        if letter[0] == "s":
            s.append(letter)
        if letter[0] == "t":
            t.append(letter)
        if letter[0] == "u":
            u.append(letter)   
        if letter[0] == "v":
            v.append(letter) 
        if letter[0] == "w":
            w.append(letter)
        if letter[0] == "x":
            x.append(letter)  
        if letter[0] == "y":
            y.append(letter) 
        if letter[0] == "z":
            z.append(letter)
    
    return [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]



if __name__ == "__main__":
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
    for i in split_first_char(word_list):
        for j in i:
            if len(i)>1:
                print(j)