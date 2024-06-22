// WRITE A PROGRAM TO FIND THE MINIMUM OF SOME ARRAYS AND SHOW ANOTHER ARRAY IN WHICH THE MIN ARE STORED.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    list<int> resultArray, mainArray = {1, 2, 3, 4};

    int sumOfElementsOfMainArray = 0;
    for (int element : mainArray)
    {
        sumOfElementsOfMainArray += element;
    }

    for (unsigned int i = 0; i < mainArray.size(); i++)
    {
        for (unsigned int innerIndex = i; innerIndex < mainArray.size(); innerIndex++)
        {
            list<int> subArray;
            list<list<int>> arrayOfSubArrays;
            auto start = next(mainArray.begin(), i);
            auto end = next(mainArray.begin(), innerIndex + 1);
            for (; start != end; ++start)
            {
                subArray.push_back(*start);
            }
            arrayOfSubArrays.push_back(subArray);

            list<int> minCollector;
            for (auto array : arrayOfSubArrays)
            {
                int maxOfChildArray = 0;
                for (auto integer : array)
                {
                    if (maxOfChildArray < integer)
                    {
                        maxOfChildArray = integer;
                    }
                }

                int min = maxOfChildArray;
                for (auto integer : array)
                {
                    if (integer < min)
                    {
                        min = integer;
                    }
                }
                minCollector.push_back(min);
            }

            int maxOfMinCollector = 0;
            for (auto integer : minCollector)
            {
                if (maxOfMinCollector < integer)
                {
                    maxOfMinCollector = integer;
                }
            }

            resultArray.push_back(maxOfMinCollector);
        }
    }

    cout << "The resultant array is : "
         << "[ ";
    for (auto integer : resultArray)
    {
        cout << integer << " ";
    }
    cout << " ]";

    return 0;
}
