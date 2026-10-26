"""Validate a small JSON-like dataset for retrieval/answer evaluation."""
REQUIRED={'question','expected_source_ids'}

def validate_dataset(records):
    if not isinstance(records,list): raise ValueError('Dataset must be a list of records.')
    errors=[]
    for i,row in enumerate(records):
        if not isinstance(row,dict): errors.append(f'row {i}: expected object'); continue
        missing=REQUIRED-row.keys()
        if missing: errors.append(f'row {i}: missing {", ".join(sorted(missing))}')
        if 'question' in row and (not isinstance(row['question'],str) or not row['question'].strip()): errors.append(f'row {i}: question must be non-empty text')
        if 'expected_source_ids' in row and (not isinstance(row['expected_source_ids'],list) or not all(isinstance(x,str) for x in row['expected_source_ids'])): errors.append(f'row {i}: expected_source_ids must be a list of strings')
    return errors

def recall_at_k(expected, retrieved, k):
    """Return Recall@k, or None when no expected source IDs exist.

    An empty gold-standard set has an undefined recall denominator, so it is
    deliberately not scored as zero or one.
    """
    if isinstance(k,bool) or not isinstance(k,int) or k<1: raise ValueError('k must be a positive integer.')
    expected=set(expected)
    if not expected: return None
    return len(expected.intersection(retrieved[:k]))/len(expected)
