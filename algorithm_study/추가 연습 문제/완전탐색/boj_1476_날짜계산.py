e, s, m = map(int, input().split())

e_o, s_o, m_o = 1, 1, 1
year = 1


while e_o != e or s_o != s or m_o != m:
    if e_o != 15:
        e_o += 1
    else:
        e_o = 1
    if s_o != 28:
        s_o += 1
    else:
        s_o = 1
    if m_o != 19:
        m_o += 1
    else:
        m_o = 1
    year += 1

print(year)

# ;;; 이게 되네