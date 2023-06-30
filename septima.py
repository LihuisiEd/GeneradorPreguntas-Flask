import spacy
import random

nlp = spacy.load("es_core_news_sm")

def generar_preguntas(texto, cantidad_preguntas):
    doc = nlp(texto)
    preguntas = []
    
    entidades = [ent.text for ent in doc.ents]
    sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
    adjetivos = [token.text for token in doc if token.pos_ == "ADJ"]
    verbos = [token.text for token in doc if token.pos_ == "VERB"]

    filtro_entidades = ["Si o si", "Si", "Sí", "Hola", "El", "Él","Adiós"]
    filtro_sustantivos = ["ganas", "día", "vas", "mano"]
    filtro_adjetivos = ["novato", "vas"]
    filtro_verbos = ["tienes", "hacer", "hagas", "tiene", "vas", "dejo", "chao", "chau", "adios"]

    for entidad in entidades:
        if entidad not in filtro_entidades:
            pregunta1 = f"¿Cuál es la relación de {entidad} con el tema del video?"
            pregunta2 = f"¿Puedes mencionar ejemplos específicos de {entidad} relacionados con el tema?"
            pregunta3 = f"¿Qué importancia tiene {entidad} en el video?"
            preguntas.extend([pregunta1, pregunta2, pregunta3])
    
    for sustantivo in sustantivos:
        if sustantivo not in filtro_sustantivos:
            pregunta1 = f"¿Puedes dar más ejemplos de {sustantivo} en relación con el tema?"
            pregunta2 = f"¿A qué se refiere '{sustantivo}' en el contexto del video?"
            pregunta3 = f"¿Cómo influye {sustantivo} en el tema abordado?"
            preguntas.extend([pregunta1, pregunta2, pregunta3])
    
    for adjetivo in adjetivos:
        if adjetivo not in filtro_adjetivos:
            pregunta1 = f"¿Cómo describirías el tema del texto con el adjetivo '{adjetivo}'?"
            pregunta2 = f"¿Puedes proporcionar más detalles sobre el tema utilizando el adjetivo '{adjetivo}'?"
            pregunta3 = f"¿Qué características se pueden asociar con el adjetivo '{adjetivo}' en el video?"
            preguntas.extend([pregunta1, pregunta2, pregunta3])
    
    for verbo in verbos:
        if verbo not in filtro_verbos:
            pregunta1 = f"¿Qué acciones relacionadas con el tema se mencionan con el verbo '{verbo}'?"
            pregunta2 = f"¿Puedes usar el verbo '{verbo}' para formular una pregunta relacionada con el tema?"
            pregunta3 = f"¿Cómo contribuye el verbo '{verbo}' al desarrollo del tema?"
            preguntas.extend([pregunta1, pregunta2, pregunta3])
    
    random.shuffle(preguntas)
    preguntas_seleccionadas = preguntas[:cantidad_preguntas]
    
    return preguntas_seleccionadas



"""
def generar_preguntas(texto, cantidad_preguntas):
    doc = nlp(texto)
    preguntas = []
    
    entidades = [ent.text for ent in doc.ents]
    sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
    adjetivos = [token.text for token in doc if token.pos_ == "ADJ"]
    verbos = [token.text for token in doc if token.pos_ == "VERB"]
    
    # Generar preguntas sobre entidades
    for entidad in entidades:
        pregunta1 = f"¿Cuál es la relación entre {entidad} y el tema del texto?"
        pregunta2 = f"¿Puedes dar ejemplos específicos de {entidad} relacionados con el tema del texto?"
        preguntas.extend([pregunta1, pregunta2])
    
    # Generar preguntas sobre sustantivos
    for sustantivo in sustantivos:
        pregunta1 = f"¿Puedes mencionar otros ejemplos de {sustantivo} relacionados con el tema del video?"
        pregunta2 = f"¿En el video mencionan '{sustantivo}', a qué se refiere en el contexto del video?"
        preguntas.extend([pregunta1, pregunta2])
    
    # Generar preguntas sobre adjetivos
    for adjetivo in adjetivos:
        pregunta1 = f"¿Cómo describirías el tema del texto usando el adjetivo '{adjetivo}'?"
        pregunta2 = f"¿Puedes proporcionar más detalles sobre el tema del texto utilizando el adjetivo '{adjetivo}'?"
        preguntas.extend([pregunta1, pregunta2])
    
    # Generar preguntas sobre verbos
    for verbo in verbos:
        pregunta1 = f"¿Qué acciones relacionadas con el tema del texto se mencionan con el verbo '{verbo}'?"
        pregunta2 = f"¿Puedes utilizar este verbo en una pregunta relacionada con el tema del texto?"
        preguntas.extend([pregunta1, pregunta2])
    
    random.shuffle(preguntas)
    preguntas_seleccionadas = preguntas[:cantidad_preguntas]
    
    return preguntas_seleccionadas

"""
