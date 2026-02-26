import spacy

from column_intelligence.nlp.semantic_anchors import SEMANTIC_ANCHORS

nlp = spacy.load("en_core_web_md")
doc = nlp("homme")


score1 = nlp("revenue").similarity(nlp("income"))  # high score
score2 = nlp("revenue").similarity(nlp("city"))  # low score

print(f"Similarity between 'revenue' and 'income': {score1:.4f}")
print(f"Similarity between 'revenue' and 'city': {score2:.4f}")


def build_anchor_vectors(nlp):
    return {
        category: [nlp(term).vector for term in terms]  # List comprehension
        for category, terms in SEMANTIC_ANCHORS.items()  # Dictionary comprehension
    }


print(build_anchor_vectors(nlp))
# ent.label is important
#
