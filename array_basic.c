# include <stdio.h>
# include <stdbool.h>

void menu(void){
    printf("\n1. Insert\n2. Delete\n3. Search\n4. Count the elements in the array\n5. Exit\n Select your choice: ");
}

int main(void) {
    int array[8];
    int choice;

    while (true){
        menu();
        scanf("%d", &choice);
    
        switch (choice) {
            case 1: printf("\nInsert");
                   break;
            case 2: printf("\nDelete");
                   break;
            case 3: printf("\nSearch");
                   break;
            case 4: printf("\nCount the number of elements in the array");
                break;
        case 5: return 0;
        default: printf("Wrong option. Try again");
      }
    }
}

OUTPUT:

1. Insert
2. Delete
3. Search
4. Count the elements in the array
5. Exit
 Select your choice: 4
