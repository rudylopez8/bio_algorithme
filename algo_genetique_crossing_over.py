import random
import string
import datetime
import os
#import psutil  # Importez le module psutil

# Paramètres de l'algorithme génétique
population_size = 100
mutation_rate = 0.01
target_length = 100  # Longueur du mot cible

def generate_random_word(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def calculate_apte(word, target):
    return sum(1 for a, b in zip(word, target) if a == b)

def mutate_word(word, mutation_rate):
    mutated_word = list(word)
    for i in range(len(mutated_word)):
        if random.random() < mutation_rate:
            mutated_word[i] = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join(mutated_word)

def algorithme_genetique_croiser(target_length, target):
    taille_population = population_size
    taux_mutation = mutation_rate

    parents_a_reproduire = taille_population // 2
    generations = 0

    def creer_enfant(longueur):
        return ''.join(random.choice(string.ascii_letters) for _ in range(longueur))

    def evaluer_fitness(enfant):
        if isinstance(enfant, str):  # Vérifier le type de l'enfant
            fitness = sum(1 for a, b in zip(enfant, target) if a == b)
            return fitness
        else:
            return 0

    def selection_parents(population, n_parents):
        parents = sorted(population, key=lambda x: evaluer_fitness(x), reverse=True)
        return parents[:n_parents]

    def croiser(parent1, parent2):
        enfant1 = ""
        enfant2 = ""

        for i in range(len(parent1)):
            if i % 2 == 0:
                enfant1 += parent1[i]
                enfant2 += parent2[i]
            else:
                enfant1 += parent2[i]
                enfant2 += parent1[i]

        return enfant1, enfant2

    def muter(enfant):
        index_mutation = random.randint(0, len(enfant) - 1)
        nouveau_caractere = random.choice(string.ascii_letters)
        enfant_mute = enfant[:index_mutation] + nouveau_caractere + enfant[index_mutation + 1:]
        return enfant_mute

    target_word = 'g' * target_length  # Le mot cible est constitué de 'g' répété target_length fois

    # Gérer la création de fichiers avec des numéros incrémentiels
    file_name = "resultatAlgoGParam"
    file_number = 1

    while os.path.exists(f"{file_name}{file_number}.txt"):
        file_number += 1

    results_file = open(f"{file_name}{file_number}.txt", "w")  # Utilisez le mode write ('w')
        
    # Écrire les paramètres de l'algorithme dans le fichier
    results_file.write(f"Paramètres de l'algorithme génétique :\n")
    results_file.write(f"Taille de la population : {population_size}\n")
    results_file.write(f"Taux de mutation : {mutation_rate}\n")
    results_file.write(f"Longueur du mot cible : {target_length}\n\n")

    population = [creer_enfant(target_length) for _ in range(taille_population)]  # Initialiser la population

    while True:
        parents = selection_parents(population, parents_a_reproduire)
        nouveaux_enfants = []

        for i in range(0, parents_a_reproduire, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]

            enfant1, enfant2 = croiser(parent1, parent2)

            if random.random() < taux_mutation:
                enfant1 = muter(enfant1)
            if random.random() < taux_mutation:
                enfant2 = muter(enfant2)

            nouveaux_enfants.extend([enfant1, enfant2])

        population = sorted(population, key=lambda x: evaluer_fitness(x), reverse=True)
        population[-len(nouveaux_enfants):] = nouveaux_enfants

        meilleur_enfant = population[0]
        generations += 1

        aptitude_meilleur_enfant = evaluer_fitness(meilleur_enfant)

        # Obtenez la température du système
        #temperature = psutil.sensors_temperatures()

        now = datetime.datetime.now()
        result_str = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Génération {generations}: Meilleur aptitude = {aptitude_meilleur_enfant}"
        
        # Écrire le meilleur individu de la génération dans le fichier
        results_file.write(result_str + "\n")
        results_file.flush()  # Assurez-vous que l'écriture est effectuée immédiatement

        if aptitude_meilleur_enfant == target_length:
            now = datetime.datetime.now()
            result_str = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Le mot cible a été trouvé à la Génération {generations} !"
            print(result_str)
            results_file.write(result_str + "\n")  # Écrire le résultat directement dans le fichier
            results_file.flush()  # Assurez-vous que l'écriture est effectuée immédiatement
            break

    results_file.close()

def main():
    target = 'g' * target_length  # Définir le mot cible correctement
    algorithme_genetique_croiser(target_length, target)

if __name__ == "__main__":
    main()
