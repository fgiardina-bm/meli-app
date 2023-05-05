from Storage import Storage
storage=Storage('meli')
cnt_col = storage.get_all_cnt_firestore()
print(f"Cnt COLLECTION: {cnt_col['count']}")