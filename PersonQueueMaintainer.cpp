#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<string>
#define MAX 10
using namespace std;

void queue_insert();
void queue_delete();
void display();
void queue_search();
string queue_array[MAX];
int rear = - 1;
int front = - 1;

int main()
{
	int choice;
	while (1)
	{
	    cout << "1.Add person to queue \n";
            cout << "2.Delete person from queue \n";
            cout << "3.Display all person in queue \n";
            cout << "4.Search for a person in queue \n";
            cout << "5.Quit \n\n";
            cout << "Enter your choice : ";
            cin >> choice;
            cout << "\n\n";
            switch (choice)
            {
		case 1:
		    queue_insert();
		    cout << "\n\nPress any key to continue...";
       		    getch();
	            system("cls");
	            break;
		case 2:
                    queue_delete();
		    cout << "\n\nPress any key to continue...";
		    getch();
		    system("cls");
		    break;
		case 3:
		    display();
		    cout << "\n\nPress any key to continue...";
		    getch();
		    system("cls");
		    break;
 		case 4:
		    queue_search();
		    cout << "\n\nPress any key to continue...";
  		    getch();
		    system("cls");
		    break;
		case 5:
		    exit(1);
		default:
		    cout << "Wrong choice \n";
		    cout << "\n\nPress any key to continue...";
		    getch();
		    system("cls");
    		}
	    }
	    return 0;
	}

        void queue_insert()
	{
	    string add_item;
	    if (rear == MAX - 1)
	    cout << "Queue Overflow \n";
	    else
	    {
		if (front == - 1)
		/*If queue is initially empty */
		front = 0;
		cout << "Insert the element in queue : ";
		cin >> add_item;
		rear = rear + 1;
		queue_array[rear] = add_item;
		cout << "\nElement inserted!";
	    }
        } /* End of queue_insert() */

	void queue_delete()
	{
	    if (front == - 1 || front > rear)
	    {
		cout << "Queue Underflow \n";
		return ;
	    }
	    else
	    {
		cout << "Element deleted from queue is : " << queue_array[front] << endl;
		front = front + 1;
		if(front == rear){
		    front = -1;
		    rear = -1;
	        }
            }
       }

	void display()
	{
	    cout << "The queue is : ";
 	    for (int i = front; i <= rear; i++)
		cout << queue_array[i] << " ";
	    cout << "\n";
	}

	void queue_search()
	{
	    cout << "Enter name of person you want to search : ";
	    string person;
	    cin >> person;
            cout << endl;
            for (int i = front; i <= rear; i++){
                if(queue_array[i] == person){
                    cout << "Person is waiting at position : " << i+1 << endl;
		    goto finish;
                }
            }
            cout << "Person is not in the queue" << endl;
	    finish:
            cout << "";
       }