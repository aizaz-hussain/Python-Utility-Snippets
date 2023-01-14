
# Extract column names
# Extract from tables and joins
# Extract where clause


sqlPath = './test.sql'


def read_sql():
    cols = ''
    whr=''
    frm = ''
    alias = False
    lstCols = []
    sql = open(sqlPath, 'r').read().lower().replace('\n', ' ')


    try:

        for idx in range(sql.index('select') + len('select') + 1, sql.index('from')):
            cols = cols + sql[idx]

        if sql.index('where'):
            for idx in range(sql.index('from') + len('from') + 1, sql.index('where')):
                frm = frm + sql[idx]

            for idx in range(sql.index('where') + len('where') + 1, len(sql)):
                whr = whr + sql[idx]

    except ValueError:
        for idx in range(sql.index('from') + len('from') + 1, len(sql)):
            frm = frm + sql[idx]

    if alias == False:
        lstCols = cols.split(' ')
        print(lstCols)
        for idx in range(len(lstCols)):
            if lstCols[idx] == 'as':
                del lstCols[idx]
                del lstCols[idx+1]


read_sql()
