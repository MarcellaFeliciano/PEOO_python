#script Python que utilize a mesma string ‘s’ do exercício anterior e exiba como resultado o seu nome e sobrenome.
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "
nome = s[s.index("M")] + s[s.index("A")] + s[s.index("R")] + s[s.index("C")] + s[s.index("E")] + s[s.index("L")] + s[s.index("L")] + s[s.index("A")]
sobrenome = s[s.index("P")] + s[s.index("E")] + s[s.index("R")] + s[s.index("E")] + s[s.index("I")] + s[s.index("R")] + s[s.index("A")]
print(nome + " " + sobrenome)

