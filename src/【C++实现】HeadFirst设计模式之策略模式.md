---
layout: post
title: 【C++实现】HeadFirst设计模式之策略模式
categories: 
  - Tech
tags: 
  - C++
  - 设计模式
date: 2014-06-05 22:48:12
---


> **策略模式**定义了算法家族，分别封装起来，让它们之间可以相互替换，此模式让算法的变化独立于使用算法的客户。

Head First设计模式中介绍策略模式时以Duck类作为例子，其中用flyBehavior和quackBehavior两个接口引用变量代表鸭子飞行和鸭子叫这两种行为，通过改变flyBehavior和quackBehavior来满足不同的Duck子类的不同行为，这样带来的好处就是可以在运行时改变Duck子类的行为。下面是我用C++改写的代码。

```C++
//MyDuck.h
#ifndef MYDUCK_INCLUDED
#define MYDUCK_INCLUDED

//在这里我用抽象类代替原文中的接口
class FlyBehavior{
	public:
		virtual void fly()=0;
};
class QuackBehavior{
	public:
		virtual void quack()=0;
};
class FlyWithWings:public FlyBehavior{
	public:
		void fly();
};
class FlyNoWay:public FlyBehavior{
	public:
		void fly();
};
class FlyRocketPowerd:public FlyBehavior{
	public:
		void fly();
};
class Quack:public QuackBehavior{
	public:
		void quack();
};
class Squeak:public QuackBehavior{
	public:
		void quack();
};
class MuteQuack:public QuackBehavior{
	public:
		void quack();
};
class Duck{
	public:
		Duck();
		void swim();
		virtual void display()=0;
		void performQuack();
		void performFly();
		void setQuackBehavior(QuackBehavior *newBehavior);
		void setFlyBehavior(FlyBehavior *newBehavior);
	//在这里我用基类指针代替原文中的接口引用变量
	protected:
		FlyBehavior *flyBehavior;
		QuackBehavior *quackBehavior;
};
class MallardDuck:public Duck{
	public:
		virtual void display();
		MallardDuck();
};
#endif // MYDUCK_INCLUDED
```

```C++
////MyDuck.cpp
#include "MyDuck"
#include <iostream>
using std::cout;
using std::endl;
//定义行为类
void FlyWithWings::fly(){
	cout<<"I'm flying with wings!!"<<endl;
}
void FlyNoWay::fly(){
	cout<<"I can't fly5555!!"<<endl;
}
void FlyRocketPowerd::fly(){
	cout<<"I'm flying with a ROCKET!!"<<endl;
}
void Quack::quack(){
	cout<<"Quack!!!"<<endl;
}
void Squeak::quack(){
	cout<<"Squeak!!!"<<endl;
}
void MuteQuack::quack(){
	cout<<"MuteQuack!!!"<<endl;
}
//定义Duck类的成员方法
void Duck::swim(){
	cout<<"I'm swimming!!!"<<endl;
}
void Duck::performQuack(){
	quackBehavior->quack();
}
void Duck::performFly(){
	flyBehavior->fly();
}
void Duck::setFlyBehavior(FlyBehavior *newBehavior){
	flyBehavior=newBehavior;
}
void Duck::setQuackBehavior(QuackBehavior *newBehavior){
	quackBehavior=newBehavior;
}
Duck::Duck(){
}
//定义MallardDuck类的成员方法
void MallardDuck::display(){
	cout<<"I'm MallardDuck!!!"<<endl;
}
MallardDuck::MallardDuck(){
	flyBehavior=new FlyWithWings;
	quackBehavior=new Quack;
}
```

```C++
//MyDuckMain.cpp
#include "MyDuck"
int main()
{
	Duck *mallard=new MallardDuck;
	mallard->display();
	mallard->performFly();
	mallard->performQuack();
	mallard->swim();
	mallard->setFlyBehavior(new FlyNoWay);
	mallard->performFly();
	mallard->setFlyBehavior(new FlyRocketPowerd);
	mallard->performFly();
	return 0;
}
```

运行结果为：
```
I'm MallardDuck!!!
I'm flying with wings!!
Quack!!!
I'm swimming!!!
I can't fly5555!!
I'm flying with a ROCKET!!
```

相关链接：[http://blog.csdn.net/zhangzijiejiayou/article/details/27306819](http://blog.csdn.net/zhangzijiejiayou/article/details/27306819)