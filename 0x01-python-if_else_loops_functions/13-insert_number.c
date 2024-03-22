#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *new = malloc(sizeof(listint_t));

if (new == NULL)
{
return (NULL);
}
if (head == NULL)
{
return (NULL);
}
new->n = number;
new->next = NULL;
if (head == NULL || (*head)->n >= number)
{
new->next = *head;
*head = new;
return (*head);
}
while (current->next != NULL && current->next->n < number)
{
current = current->next;
}
new->next = current->next;
current->next = new;
return (*head);
}
