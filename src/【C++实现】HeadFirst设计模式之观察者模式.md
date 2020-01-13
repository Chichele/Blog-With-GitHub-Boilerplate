---
layout: post
title: 【C++实现】HeadFirst设计模式之观察者模式
categories: 
  - Tech
tags: 
  - 设计模式
  - C++
date: 2014-08-02 14:42:15
---

> **观察者模式**定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，它的所有依赖者都会收到通知并自动更新。

一方可称为主题（subject），另一方可称为观察者（observer），一个主题可拥有多个观察者。当主题的数据有变动时，就会通知所有订阅了它的观察者。在这之后的操作有两种：

*   推：主题直接将数据推送给所有观察者。
*   拉：主题通知了所有观察者后，每个观察者再根据自己的需要从主题拉取所需数据。

下面是我用C++实现的代码，其中的update方法采用了“拉”的方式从主题获取数据。

```C++
//MyObserver.h
#ifndef MYOBSERVER_H_INCLUDED
#define MYOBSERVER_H_INCLUDED

#include<iostream>
#include<vector>
#define TRUE 1;
#define FALSE 0;

class MyObserver{
    public:
        virtual void update();
        virtual void display();
};

class MyObservable{
    protected:
        std::vector<MyObserver*>observers;
    public:
        //MyObservable();
        ~MyObservable();
        int addObserver(MyObserver* obs);
        int deleteObserver(MyObserver* obs);
        int notifyObservers();

};
#endif // MYOBSERVER_H_INCLUDED
```

```C++
//MyObserver.cpp
#include "MyObserver.h"
using std::cout;
using std::vector;

void MyObserver::update(){
    cout<<"I'm update method ofbase class.\n";
}
void MyObserver::display(){
    cout<<"I'm display method ofbase class.\n";
}

MyObservable::~MyObservable(){
    observers.clear();
}
int MyObservable::addObserver(MyObserver* obs){
    observers.push_back(*obs);
    return TRUE;
}
int MyObservable::deleteObserver(MyObserver* obs){
    for(vector<MyObserver*>::iterator it = observers.begin();it != observers.end();++it){
        if((*it) == *obs){
            observers.erase(it);
            return TRUE;
        }
    }
    return FALSE;
}
 int MyObservable::notifyObservers(){
    for(vector<MyObserver*>::iterator it = observers.begin();it != observers.end();++it){
        (*it)->update();
    }
    return TRUE;
}
```

```C++
//main.cpp
//#include <iostream>
#include "MyObserver.h"
using std::cout;
using std::endl;
class WeatherData:public MyObservable{
    private:
        float temperature;
        float humidity;
        float pressure;
    public:
        void setMeasurements(float temperature,float humidity,float pressure){
            this->temperature=temperature;
            this->humidity=humidity;
            this->pressure=pressure;
            measurementsChanged();
        }
        void measurementsChanged(){
            notifyObservers();
        }
        float getTemperature(){
            return temperature;
        }
        float getHumidity(){
            return humidity;
        }
        float getPressure(){
            return pressure;
        }
};

class CurrentDisplay:public MyObserver{
    private:
        WeatherData* weatherData;
        float temperature;
        float humidity;
        float pressure;
    public:
        CurrentDisplay(WeatherData* weatherData){
            this->weatherData=*weatherData;
            this->weatherData->addObserver(*this);
        }
        CurrentDisplay(){
            cout<<"You have to give a parameter.\n";
        }
        ~CurrentDisplay(){
            weatherData->deleteObserver(*this);
        }
        void update(){
            temperature=weatherData->getTemperature();
            humidity=weatherData->getHumidity();
            pressure=weatherData->getPressure();
            display();
        }
        void display(){
            cout<<"temperature:"<<temperature<<"\nhumidity:"<<humidity<<"\npressure:"<<pressure<<endl;
        }
};
int main()
{
    WeatherData weatherdata;
    CurrentDisplay currentdisplay(weatherdata);
    weatherdata.setMeasurements(80,65,30.4);
    weatherdata.setMeasurements(82,70,29.2);
    weatherdata.setMeasurements(78,90,29.2);
    currentdisplay.~CurrentDisplay();
    CurrentDisplay test2(weatherdata);
    weatherdata.setMeasurements(78,912,29.2);
    return 0;
}
```