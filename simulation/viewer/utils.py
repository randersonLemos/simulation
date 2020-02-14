def filter_xtikcs(code, step):
    head = 'xtick={'
    bgn = code.find(head)+len(head)
    end = code.find('}',bgn)
    old = code[bgn:end]
    new = ','.join(old.split(',')[::step])
    code =  code.replace(old, new)

    head = 'xticklabels={'
    bgn = code.find(head)+len(head)
    end = code.find('}',bgn)
    old = code[bgn:end]
    new = ','.join(old.split(',')[::step])
    code =  code.replace(old, new)
    return code
