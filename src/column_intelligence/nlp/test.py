from loader import get_nlp, get_anchor_vecs

model = get_nlp()
anchor_vecs = get_anchor_vecs()
sentence_vecs = model.encode("villes", convert_to_numpy=True)


def get_max(similarities_dict: dict[str, float]) -> str:
    max_category = None
    max_similarity = -float("inf")

    for category, similarity in similarities_dict.items():
        if similarity > max_similarity:
            max_similarity = similarity
            max_category = category

    return {"Category": max_category, "Score": max_similarity}


similarities_dict = {
    category: model.similarity(sentence_vecs, anchor_vec)
    for category, anchor_vec in anchor_vecs.items()
}

print(get_max(similarities_dict))
