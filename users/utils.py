


def get_document_choices():
    CITIZENSHIP_CARD='CC'
    PASSPORT='PAS'
    FOREIGN_ID='FID'
    NIT='NIT'

    DOCUMENT_CHOICES = [
        (CITIZENSHIP_CARD, 'Citizenship card'),
        (PASSPORT, 'Passport'),
        (FOREIGN_ID, 'Foreigner ID'),
        (NIT, 'NIT'),
    ]
    return DOCUMENT_CHOICES