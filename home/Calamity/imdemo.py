i01.integratedMovement.removeObject("pole")
i01.integratedMovement.removeAi("kinect",i01.integratedMovement.Ai.AVOID_COLLISION)
i01.rest()
sleep(3)
i01.integratedMovement.moveTo("rightArm",-300,500,400)
mouth.speakBlocking("Hello, I am vinmoov")
sleep(3)
i01.rest()
mouth.speakBlocking("I want to talk to you about a new myrobotlab service called Integrated Movement")
mouth.speakBlocking("With this service, I can move my hand to a point in space by using inverse kinematics")
i01.integratedMovement.moveTo("leftArm",500,500,600)
mouth.speakBlocking("you don't have to specify how I move each of my joint. You just told me where to move")
i01.rest()
i01.integratedMovement.addObject(-200,500, -1000,-200,500,1000,"pole",30,True)
mouth.speakBlocking("Look! Something appear in my field of view. It's a pole so I can do some pole dancing.")
mouth.speakBlocking("But that's for another private video called Sexy Dancing Robots.")
mouth.speakBlocking("The Integrated Movement service allow to add objects in my surrounding so I can interract with them")
i01.integratedMovement.moveTo("rightArm","pole",i01.integratedMovement.ObjectPointLocation.CENTER_SIDE)
mouth.speakBlocking("I can move my hand close to that item. I can also see objects in my surrounding using the kinect I have in my belly.")
i01.integratedMovement.moveTo("rightArm",-600,600,400)
sleep(3)
i01.torso.midStom.setVelocity(3)
i01.torso.midStom.moveTo(30)
mouth.speakBlocking("I can also react if my arm enter in collision with an object I know of")
sleep(10)
i01.rest()
mouth.speakBlocking("I can also try to control where my center of gravity is. When I am in this position, my center of gravity is right in the middle of my belly")
mouth.speakBlocking("So I'm standing in a stable position. But if I raise my arm, my center of gravity will shift away and if it get too far from my center point")
mouth.speakBlocking("I may tip over and fall if my base is not fixed strong enough")
mouth.speakBlocking("If one of my arm is set to keep balance in integrated movement service, I can adjust my position to keep my center of gravity close to my center point")
mouth.speakBlocking("that way, I will be able to stand in a more stable position")
i01.integratedMovement.setAi("rightArm",i01.integratedMovement.Ai.KEEP_BALANCE)
i01.leftArm.omoplate.moveTo(70)
i01.leftArm.rotate.moveTo(180)
i01.leftArm.bicep.moveTo(40)
i01.torso.topStom.moveTo(80)





