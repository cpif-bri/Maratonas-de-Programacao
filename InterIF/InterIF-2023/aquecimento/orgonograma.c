#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definição de uma estrutura para um nó da árvore
typedef struct TreeNode {
    char* data; // Nome do setor
    struct TreeNode* firstChild;  // Ponteiro para o primeiro setor sob responsabilidade
    struct TreeNode* nextSibling; // Ponteiro para o próximo setor sob responsabilidade do mesmo pai
} TreeNode;

// Função para criar um novo nó da árvore
TreeNode* createTreeNode(const char* data) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->data = strdup(data); // Copiar a string para o novo nó
    newNode->firstChild = NULL;
    newNode->nextSibling = NULL;
    return newNode;
}

// Função para adicionar um filho ordenadamente em ordem alfabética
void addChildOrdered(TreeNode* parent, TreeNode* child) {
    if (parent == NULL || child == NULL) {
        return;
    }

    // Caso especial: a lista de filhos está vazia ou o novo filho deve ser o primeiro
    if (parent->firstChild == NULL || strcmp(child->data, parent->firstChild->data) < 0) {
        child->nextSibling = parent->firstChild;
        parent->firstChild = child;
    } else {
        TreeNode* current = parent->firstChild;
        TreeNode* prev = NULL;

        while (current != NULL && strcmp(child->data, current->data) > 0) {
            prev = current;
            current = current->nextSibling;
        }

        prev->nextSibling = child;
        child->nextSibling = current;
    }
}

// Função para encontrar um setor com base no nome
TreeNode* findSector(TreeNode* root, const char* value) {
    if (root == NULL || value == NULL) {
        return NULL;
    }

    if (strcmp(root->data, value) == 0) {
        return root;
    }

    TreeNode* child = root->firstChild;
    while (child != NULL) {
        TreeNode* result = findSector(child, value);
        if (result != NULL) {
            return result;
        }
        child = child->nextSibling;
    }

    return NULL;
}

// Função para imprimir a hierarquia de setores em ordem alfabética
void printHierarchy(TreeNode* node) {
    if (node == NULL) {
        return;
    }

    printf("%s\n", node->data);

    TreeNode* child = node->firstChild;
    while (child != NULL) {
        printHierarchy(child);
        child = child->nextSibling;
    }
}

// Função para liberar a memória da árvore
void freeTree(TreeNode* root) {
    if (root == NULL) {
        return;
    }

    freeTree(root->firstChild);
    freeTree(root->nextSibling);

    free(root->data);
    free(root);
}

int main() {
    char sectorName[40];
    TreeNode* root = NULL;

    // Ler o nome do setor mais alto na hierarquia
    scanf("%s", sectorName);
    root = createTreeNode(sectorName);

    // Ler os setores e suas responsabilidades
    while (1) {
        char parentName[40];
        scanf("%s %s", sectorName, parentName);
        if (strcmp(sectorName, "fim") == 0 && strcmp(parentName, "entrada") == 0) {
            break;
        }

        TreeNode* parent = findSector(root, parentName);
        TreeNode* child = createTreeNode(sectorName);

        if (parent != NULL) {
            addChildOrdered(parent, child);
        }
    }

    // Ler o nome do setor a ser pesquisado
    scanf("%s", sectorName);

    // Encontrar o setor e imprimir a hierarquia
    TreeNode* sectorToFind = findSector(root, sectorName);
    if (sectorToFind != NULL) {
        printHierarchy(sectorToFind);
    }

    // Liberar a memória alocada
    freeTree(root);

    return 0;
}
