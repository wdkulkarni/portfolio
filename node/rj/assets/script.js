var romeo;
var juliet;
var benvolio;
var ladycap;
var tybalt;
var ladymont;
var nurse;
var capulet;
var montague;
var prince;
var paris;
var mercutio;
var friar;
var apothecary;
var characters = [];
var props = [];
var rotated = [];

var bg;
var curtain = false;
var censored = false;

var floor = 250;
var wall = 1000;

var garden = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1r3-14IarBFZqR1aX30h_TV-5snJyk9FPnQ&s';
var street = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO23jhWeLBickkd4BV8YCCVa8uUesBQQKJ1Q&s';
var stage = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7r_Z9-14BeoTFNKUdyIJvDTCddaqPgnMeLQ&s';
var mansion = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBRu9pM67tYkrgkBt99mBn7A5-1-HvwN_baA&s';
var balcony = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPskY3hBOAczduK5ICN-V3yA5Y0qT3X6nf6w&s';
var cell = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIDxaS15NnbAkAYQ0cKQ1k62EvEsxYn-nDHQ&s';
var bedroom = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8aD-vLu5yVsYWPLA6nzMTJo_mqT_7wVdolg&s';

var latim = 0;

function begin() {
    romeo = new sprite(0, floor, 'blue', 'm');
    juliet = new sprite(0, floor, 'red', 'w');
    nurse = new sprite(0, floor, 'gray', 'w');
    mercutio = new sprite(0, floor, 'green', 'm');
    benvolio = new sprite(0, floor, 'blue', 'm');
    ladycap = new sprite(0, floor, 'red', 'w');
    ladymont = new sprite(0, floor, 'blue', 'w');
    capulet = new sprite(0, floor, 'red', 'm');
    montague = new sprite(0, floor, 'blue', 'm');
    prince = new sprite(0, floor, 'green', 'm');
    friar = new sprite(0, floor, 'gray', 'm');
    apothecary = new sprite(0, floor, 'gray', 'm');
    paris = new sprite(0, floor, 'green', 'm');
    tybalt = new sprite(0, floor, 'red', 'm');
    characters = [romeo, juliet, friar, paris, prince, capulet, montague, ladycap, ladymont, mercutio, benvolio, nurse, apothecary, tybalt];
    play.start();
    confirm('Do you want to start?');
    I();
    II();
    III();
    IV();
    V();
};
var play = {
    canvas : document.createElement('canvas'),
    start : function() {
        this.interval = setInterval(update, 10);
        this.canvas.width = 1000;
        this.canvas.height = 400;
        this.ctx = this.canvas.getContext('2d');
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    },
    clear : function() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
};

function V() {
    st(function() {
        bg.src = street;
        romeo.place(200);
        benvolio.place(400);
        curtain = false;
    }, 1000);
    st(function() {
        print('blue', 'Romeo: I had a dream I died and Juliet revived me.');
        print('blue', 'Balthasar: Juliet is dead.');
        print('blue', 'Romeo: I defy you stars!');
    }, 2000);
    st(function() {
        curtain = true;
        benvolio.exit();
        apothecary.place(400);
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2FcESG_JsDUSY7BQ-Q6XaSb4rppL3Lqj9gQ&s';
    }, 6000);
    st(function() {
        curtain = false;
        print('blue', 'Romeo: I need poison.');
        print('gray', 'Apothecary: I can not do it.');
        print('blue', 'Romeo: I will pay you.');
    }, 7000);
    st(function() {
        print('gray', 'Apothecary: Sure, here you go.');
    }, 11000);
    st(function() {
        curtain = true;
        bg.src = cell;
        friar.place(200);
    }, 13000);
    st(function() {
        curtain = false;
        print('gray', 'Friar Lawrence: Hey, John, you delivered my message?');
        print('gray', 'Friar John: Nah, man, I got quarantined.');
        print('gray', 'Friar Lawrence: Oh, no, it was important.');
    }, 14000);
    st(function() {
        print('gray', 'Friar Lawrence: I guess I will have to save Juliet myself.');
    }, 18000);
    st(function() {
        curtain = true;
        apothecary.exit();
        friar.exit();
        bg.src = garden;
        paris.place(400);
        romeo.place(200);
    }, 20000);
    st(function() {
        curtain = false;
        print('green', 'Paris: What are you doing here?');
        print('blue', 'Romeo: Let me go, I have important stuff to do.');
        print('green', 'Paris: No.');
    }, 21000);
    st(function() {
        romeo.enter(1);
        props.push(new sword(romeo, 'r'));
    }, 25000);
    st(function() {
        romeo.stop();
        props[0].xvel = 0;
        paris.exit();
    }, 26000);
    st(function() {
        props = [];
        romeo.enter(4);
    }, 27000);
    st(function() {
        curtain = true;
        romeo.exit();
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxLnjq23H4dFYj0bYSXU9Cow1MvcLKEalowQ&s';
        rotated.push(function () {
            play.ctx.fillStyle = 'red';
            play.ctx.fillRect(800, 350, 100, 50);
            play.ctx.fillRect(900, 350, 50, 10);
            play.ctx.fillRect(900, 390, 50, 10);
            play.ctx.fillStyle = '#ffe5b4';
            play.ctx.fillRect(765, 358, 35, 35);
            play.ctx.fillStyle = 'black';
            play.ctx.fillRect(760, 358, 5, 35);
            play.ctx.fillRect(760, 353, 50, 5);
            play.ctx.fillRect(760, 393, 50, 5);
        });
        romeo.place(700);
    }, 28000);
    st(function() {
        curtain = false;
        print('blue', 'Romeo: She still looks pretty.');
        print('blue', "Here's to my love!");
    }, 29000);
    st(function() {
        romeo.exit();
        rotated.push(function () {
            play.ctx.fillStyle = 'blue';
            play.ctx.fillRect(600, 350, 100, 50);
            play.ctx.fillRect(700, 350, 50, 10);
            play.ctx.fillRect(700, 390, 50, 10);
            play.ctx.fillStyle = '#ffe5b4';
            play.ctx.fillRect(565, 358, 35, 35);
            play.ctx.fillStyle = 'black';
            play.ctx.fillRect(560, 358, 5, 35);
        });
        friar.enter(2.5);
    }, 31000);
    st(function() {
        friar.stop();
        juliet.place(850);
        rotated.shift();
        print('red', 'Juliet: Romeo has drank poison and died.');
        print('gray', 'Friar: Juliet, we must go.');
        print('red', 'Juliet: No, I can not go.');
    }, 32000);
    st(function() {
        print('red', 'Juliet:  0 happy dagger, this is thy sheath.');
        print('red', 'There rust and let me die.');
    }, 35000);
    st(function() {
        juliet.exit();
        rotated.push(function () {
            play.ctx.fillStyle = 'red';
            play.ctx.fillRect(800, 350, 100, 50);
            play.ctx.fillRect(900, 350, 50, 10);
            play.ctx.fillRect(900, 390, 50, 10);
            play.ctx.fillStyle = '#ffe5b4';
            play.ctx.fillRect(765, 358, 35, 35);
            play.ctx.fillStyle = 'black';
            play.ctx.fillRect(760, 358, 5, 35);
            play.ctx.fillRect(760, 353, 50, 5);
            play.ctx.fillRect(760, 393, 50, 5);
        });
    }, 37000);
    st(function() {
        prince.enter(2);
        capulet.enter(1.5);
        montague.enter(1);
        ladycap.enter(.5);
    }, 38000);
    st(function() {
        prince.stop();
        capulet.stop();
        montague.stop();
        ladycap.stop();
        print('green', 'Prince: What misadventure is so early up');
        print('green', 'That calls our person from our morning rest?');
    }, 39000);
    st(function() {
        print('red', "Lady Capulet: Oh, the people in the street cry 'Romeo',");
        print('red', "Some 'Juliet,' and some 'Paris,' and all run");
        print('red', 'With open outcry toward our monument.');
    }, 41000);
    st(function() {
        print('blue', 'Montague: Alas, my liege, my wife is dead tonight.');
        print('blue', "Grief of my son's exile hath stopped her breath.");
        print('blue', 'What manners is in this, to press before thy father to a grave?');
    }, 45000);
    st(function() {
        print('green', 'Prince: Friar, can you explain what is going on?');
        print('gray', 'Friar: I am the greatest, able to do least.');
        print('gray', 'And here I stand, both to impeach and purge.');
    }, 50000);
    st(function() {
        print('gray', 'Romeo and Juliet were married.');
        print('gray', 'When Romeo got exiled, and Juliet was pushed to marry, she came to me.');
        print('gray', 'I gave her a sleeping potion, and when she was in the tomb, Romeo was to rescue her.');
    }, 54000);
    st(function() {
        print('gray', 'Romeo did not get my message though, so I came here, finding Romeo and Paris dead.');
        print('gray', 'Juliet woke up and then killed herself.');
    }, 60000);
    st(function() {
        print('green', 'Prince: See what a scourge is laid upon your hate,');
        print('green', 'That heaven finds means to kill your joys with love!');
    }, 64000);
    st(function() {
        print('green', 'And I, for winking at your discords, too');
        print('green', 'Have lost a brace of kinsmen. All are punished.');
    }, 67000);
    st(function() {
        print('red', 'Capulet: I apologize to you, Montague.');
        print('blue', 'Montague: I am sorry too, Capulet.');
    }, 70000);
    st(function() {
        print('green', 'Prince: A glooming peace this morning with it brings.');
        print('green', 'The sun, for sorrow, will not show his head,');
        print('green', 'Go hence, to have more talk of these sad things.');
    }, 73000);
    st(function() {
        print('green', 'Some shall be pardoned, and some punished.');
        print('green', 'For never was a story of more woe');
        print('green', 'Than this of Juliet and her Romeo.');
    }, 77000);
    st(function() {
        curtain = true;
        capulet.exit();
        montague.exit();
        ladycap.exit();
        friar.exit();
        prince.exit();
        rotated = [];
    }, 81000);
    latim += 81000;
};

function IV() {
    st(function() {
        bg.src = cell;
        friar.place(400);
        paris.place(600);
        juliet.place(200);
    }, 1000);
    st(function() {
        curtain = false;
        print('green', 'Paris: Oh, hey, Juliet, I was just telling the Friar how we are getting married.');
        print('red', 'Juliet: Yeah, okay, cool.');
        print('green', 'Paris: I will leave you two alone now.');
        paris.enter(1.75);
    }, 2000);
    st(function() {
        paris.stop();
        paris.exit();
        print('gray', 'Friar: Okay, I see your problem now.');
        print('gray', 'I will give you something to make it look like you are dead.');
        print('gray', 'Then Romeo will rescue you and take you to Mantua with him.');
    }, 6000);
    st(function() {
        curtain = true;
        bg.src = mansion;
        friar.exit();
        juliet.place(200);
        capulet.place(400);
    }, 10000);
    st(function() {
        curtain = false;
        print('red', 'Juliet: I will marry Paris.');
        print('red', 'Capulet: Hooray! You guys will get married tomorrow.');
    }, 11000);
    st(function() {
        curtain = true;
        bg.src = bedroom;
        capulet.exit();
    }, 14000);
    st(function() {
        curtain = false;
        print('red', 'Juliet: What if it does not work?');
        print('red', 'Or maybe it is poison.');
        print('red', 'I might wake up early and go crazy, too.');
    }, 15000);
    st(function() {
        print('red', "Romeo, Romeo, Romeo! Here's drink. I drink to thee.");
        juliet.exit();
        rotated.push(function () {
            play.ctx.fillStyle = 'red';
            play.ctx.fillRect(200, 350, 100, 50);
            play.ctx.fillRect(300, 350, 50, 10);
            play.ctx.fillRect(300, 390, 50, 10);
            play.ctx.fillStyle = '#ffe5b4';
            play.ctx.fillRect(165, 358, 35, 35);
            play.ctx.fillStyle = 'black';
            play.ctx.fillRect(160, 358, 5, 35);
            play.ctx.fillRect(160, 353, 50, 5);
            play.ctx.fillRect(160, 393, 50, 5);
        });
    }, 19000);
    st(function() {
        curtain = true;
    }, 21000);
    st(function() {
        curtain = false;
        nurse.enter(3, op=true);
    }, 22000);
    st(function() {
        nurse.stop();
        print('gray', "Nurse: Help, help! My lady's dead!");
        capulet.enter(2, op=true);
        ladycap.enter(1, op=true);
    }, 23000);
    st(function() {
        capulet.stop();
        ladycap.stop();
        print('red', 'Lady Capulet: O me, 0 me! My child, my only life!');
        print('red', 'Capulet: Death is my son-in-law. Death is my heir');
        paris.enter(1/3, op=true);
    }, 25000);
    st(function() {
        paris.stop();
        print('green', 'Paris: Beguiled, divorced, wronged, spited, slain!');
        friar.enter(.1)
    }, 28000);
    st(function() {
        friar.stop();
        print('gray', 'Friar: Everyone prepare');
        print('gray', 'To follow this fair corse unto her grave.');
    }, 30000);
    st(function() {
        curtain = true;
        friar.exit();
        rotated = [];
        paris.exit();
        capulet.exit();
        ladycap.exit();
        nurse.exit();
    }, 33000);
    latim += 33000;
};

function III() {
    st(function() {
        bg.src = street;
        benvolio.stop();
        mercutio.stop();
        benvolio.place(300);
        mercutio.place(500);
    }, 1000);
    st(function() {
        curtain = false;
        print('blue', "Benvolio: I pray thee, good Mercutio, let's retire.");
        print('blue', 'The day is hot; the Capulets, abroad;');
        print('blue', "And if we meet we shall not 'scape a brawl,");
        print('blue', 'For now, these hot days, is the mad blood stirring.');
    }, 2000);
    st(function() {
        print('green', 'Mercutio: Nah, man, a brawl is good.');
        tybalt.enter(1.5, op=true);
    }, 7000);
    st(function() {
        tybalt.stop();
        print('red', "Tybalt: Mercutio, thou consort'st with Romeo.");
        print('green', 'Mercutio: Consort? What, dost thou make us minstrels?');
        romeo.enter(1.8);
    }, 8000);
    st(function() {
        romeo.stop();
        print('red', 'Tybalt: Romeo, thou art a villain!');
    }, 11000);
    st(function() {
        print('blue', 'Romeo: Tybalt, the reason that I have to love thee');
        print('blue', 'Doth much excuse the appertaining rage');
        print('blue', 'To such a greeting. Villain am I none.');
    }, 13000);
    st(function() {
        print('blue', 'Good Capulet-which name I tender');
        print('blue', 'As dearly as my own-be satisfied.');
        print('green', 'Mercutio: Tybalt, I will fight you!');
    }, 17000);
    st(function() {
        tybalt.enter(-2.75);
    }, 21000);
    st(function() {
        tybalt.stop();
        props.push(new sword(tybalt, 'l'));
    }, 22000);
    st(function() {
        props[0].xvel = 1.5;
        tybalt.enter(1.5);
    }, 23000);
    st(function() {
        props[0].xvel = 0;
        tybalt.stop();
        props = [];
        print('green', 'Mercutio: A plague on both your house!');
    }, 24000);
    st(function() {
        mercutio.exit();
        print('blue', 'Romeo: Either thou or I, or both, must go with Mercutio.');
        romeo.enter(.5);
        props.push(new sword(romeo, 'r'));
    }, 26000);
    st(function() {
        props[0].xvel = 0;
        romeo.stop();
    }, 28000);
    st(function() {
        tybalt.exit();
        props = [];
    }, 29000);
    st(function() {
        print('blue', 'Benvolio: Run, Romeo! Otherwise the Prince will kill you!');
        print('blue', "Romeo: Oh, I am fortune's fool!");
        romeo.enter(2);
    }, 30000);
    st(function() {
        romeo.stop();
        romeo.exit();
        prince.enter(.5);
    }, 33000);
    st(function() {
        prince.stop();
        print('green', 'Prince: I say Romeo will be banished.');
    }, 34000);
    st(function() {
        curtain = true;
        prince.exit();
        benvolio.exit();
        bg.src = mansion;
        juliet.place(400);
        nurse.place(200);
    }, 36000);
    st(function() {
        curtain = false;
        print('red', 'Juliet: I am looking forward to the night.');
        print('gray', 'Nurse: He is dead!');
    }, 37000);
    st(function() {
        print('red', 'Juliet: Nooooo! My husband is dead!');
        print('gray', 'Nurse: No, Tybalt is dead.');
        print('red', 'Juliet: Oh, ok.');
    }, 41000);
    st(function() {
        print('gray', 'Nurse: But Romeo killed him and now he is banished.');
        print('red', 'Juliet: No, how could my husband do this!');
        print('red', 'Beautiful tyrant! Fiend angelical!');
    }, 44000);
    st(function() {
        print('red', 'Was ever book containing such vile matter so fairly bound?');
        print('red', 'But, I am sure he must have his reasons.');
    }, 48000);
    st(function() {
        curtain = true;
        bg.src = cell;
        romeo.place(400);
        friar.place(600);
        nurse.exit();
        juliet.exit();
    }, 51000);
    st(function() {
        curtain = false;
        print('gray', 'Friar: Romeo, the Prince has said that you are banished.');
        print('blue', 'Romeo: Noooooooooooo!');
        print('gray', 'Friar: Get a grip, man. You are not dead.');
    }, 52000);
    st(function() {
        nurse.enter(1);
    }, 56000);
    st(function() {
        nurse.stop();
        print('blue', 'Romeo: How fares my lady?');
        print('gray', 'Nurse: She does nothing but weeps and weeps.');
    }, 57000);
    st(function() {
        print('gray', 'Friar: Romeo, you should go to Juliet, see her, and then leave for Mantua.');
        print('gray', 'I will work to get you brought back.');
    }, 59000);
    st(function() {
        curtain = true;
        romeo.exit();
        nurse.exit();
        friar.exit();
        bg.src = mansion;
        capulet.place(200);
        paris.place(400);
    }, 62000);
    st(function() {
        curtain = false;
        print('red', 'Capulet: You can marry my daughter, does Thursday sound good?');
        print('green', 'Paris: My lord, I would that Thursday were tomorrow.');
    }, 63000);
    st(function() {
        curtain = true;
        bg.src = bedroom;
        paris.exit();
        capulet.exit();
        juliet.place(200);
        ladycap.place(400);
    }, 66000);
    st(function() {
        curtain = false;
        print('red', 'Lady Capulet: Juliet, you are to marry Paris.');
        print('red', 'Juliet: No!');
        print('red', 'Lady Capulet: You will, otherwise your father will disown you.');
    }, 67000);
    st(function() {
        ladycap.enter(-2);
    }, 68000)
    st(function() {
        ladycap.stop();
        ladycap.exit();
        print('red', 'Juliet: I will go to Friar Lawrence to see if he has something to help.');
    }, 70000);
    st(function() {
        curtain = true;
    }, 71000);
    latim += 71000;
};

function II() {
    st(function() {
        bg.src = stage;
        var narrator = new sprite(0, 125, 'gray', 'm');
        characters.push(narrator);
        narrator.place(200);
        curtain = false;
        print('gray', 'Romeo no longer loves Rosaline, but loves Juliet.');
    }, 1000);
    st(function() {
        curtain = true;
        characters.pop();
        bg.src = garden;
        romeo.place(400);
    }, 3000);
    st(function() {
        curtain = false;
        print('green', 'Mercutio: Romeo! Humours, madman, passion, lover!');
        print('green', 'Appear thou in the likeness of a sigh!');
    }, 4000)
    st(function() {
        print('blue', 'Romeo: He jests at scars that never felt a wound.');
    }, 7000);
    st(function() {
        curtain = true;
        bg.src = balcony;
        romeo.place(100);
        juliet.y = 50;
        juliet.place(500);
    }, 9000);
    st(function() {
        curtain = false;
        print('blue', 'Romeo: But soft! What light through yonder window breaks?');
        print('blue', 'It is the east, and Juliet is the sun.');
    }, 10000);
    st(function() {
        print('red', 'Juliet: O Romeo, Romeo! Wherefore art thou Romeo?');
        print('red', 'Deny thy father and refuse thy name.');
    }, 13000);
    st(function() {
        print('red', "What's in a name? That which we call a rose");
        print('red', 'By any other word would smell as sweet.');
    }, 15000);
    st(function() {
        print('blue', 'Romeo: I take thee at thy word.');
        print('red', 'Juliet: Oh, it is you Romeo, I got scared.');
    }, 18000);
    st(function() {
        print('red', 'Juliet: You know what, I like you, we should get married.');
        print('blue', 'Romeo: Sure.');
    }, 21000);
    st(function() {
        print('red', 'Juliet: I will send a messenger.');
        print('red', 'Goodbye, parting is such sweet sorrow.');
    }, 24000);
    st(function() {
        curtain = true;
        bg.src = cell;
        romeo.exit();
        juliet.exit();
        juliet.y = floor;
        friar.place(400);
    }, 27000);
    st(function() {
        curtain = false;
        print('gray', 'Friar: Plants are awesome.');
    }, 28000);
    st(function() {
        romeo.enter(1.5);
    }, 29000);
    st(function() {
        romeo.stop();
        print('blue', 'Romeo: Hey.');
        print('gray', 'Friar: Romeo, you have not slept, were you with Rosaline?');
    }, 30000);
    st(function() {
        print('blue', 'Romeo: No, I love someone else, Juliet, and I want to marry her.');
        print('gray', 'Friar: You love with your eyes, but I will do it to help the households get together.');
    }, 33000);
    st(function() {
        curtain = true;
        bg.src = garden;
        romeo.exit();
        friar.exit();
        mercutio.place(500);
        benvolio.place(300);
    }, 37000);
    st(function() {
        curtain = false;
        print('green', 'Mercutio: Where the devil should this Romeo be?');
        print('blue', 'Benvolio: Tybalt sent him a letter to fight.');
    }, 38000);
    st(function() {
        print('green', 'Mercutio: Romeo can not fight, I should do it for him.');
        print('blue', 'Benvolio: Oh, look there is Romeo.');
        romeo.enter(.5/3);
    }, 41000);
    st(function() {
        romeo.stop();
        print('green', 'Mercutio: You left us last night.');
        print('blue', 'Romeo: Why, no I had important things to do.');
    }, 44000);
    st(function() {
        print('green', 'Mercutio: You seem better today. You are not sad.');
        print('green', 'Now art thou sociable, now art thou Romeo.');
    }, 47000);
    st(function() {
        nurse.enter(.5, op=true);
    }, 50000);
    st(function() {
        nurse.stop();
        print('gray', 'Nurse: I need to find Romeo.');
        print('blue', 'Romeo: I am Romeo.');
        print('gray', 'Nurse: I need to talk alone with you.');
        mercutio.enter(-2);
        benvolio.enter(-1);
    }, 51000);
    st(function() {
        benvolio.exit();
        mercutio.exit();
        print('blue', 'Romeo: Tell Juliet that Friar Lawrence will marry her today.');
        print('gray', 'Nurse: Sure, she will be really happy.');
    }, 54000);
    st(function() {
        curtain = true;
        bg.src = mansion;
        romeo.exit();
        nurse.exit();
        juliet.place(500);
    }, 57000);
    st(function() {
        curtain = false;
        print('red', 'Juliet: Why is the Nurse not here yet?');
        nurse.enter(.75);
    }, 58000);
    st(function() {
        nurse.stop();
        print('red', 'Juliet: Tell me, what does Romeo say?');
        print('gray', 'Nurse: Wait, I am out of breath');
        print('red', 'Juliet: How art thou out of breath when thou hast breath');
        print('red', 'To say to me that thou art out of breath?');
    }, 60000);
    st(function() {
        print('gray', 'Nurse: Okay, I will tell you.');
        print('gray', "Romeo has said that he will marry you ate Friar Lawrence's cell.");
        print('red', 'Juliet: Hie to high fortune! Honest Nurse, farewell.');
    }, 65000);
    st(function() {
        curtain = true;
        nurse.exit();
        juliet.place(300);
        friar.place(500);
        romeo.place(700);
        bg.src = cell;
    }, 69000);
    st(function() {
        curtain = false;
        print('gray', 'Friar: Come, come with me, and we will make short work.');
        print('gray', 'For, by your leaves, you shall not stay alone');
        print('gray', 'Till holy church incorporate two in one.');
    }, 70000);
    st(function() {
        curtain = true;
        romeo.exit();
        friar.exit();
        juliet.exit();
    }, 75000);
    latim += 75000;
};

function I() {
    bg = new background(stage);
    var narrator = new sprite(0, 125, 'gray', 'm');
    var sampson = new sprite(0, floor, 'red', 'm');
    var gregory = new sprite(0, floor, 'red', 'm');
    var abram = new sprite(wall, floor, 'blue', 'm');
    characters.push(narrator);
    narrator.toupdate = true;
    narrator.xvel = 3;
    st(function() {
        narrator.xvel = 0;
        print('black', 'Two households, both alike in dignity');
    }, 1000);
    st(function() {print('black', 'In fair Verona, where we lay our scene,');}, 2000*1.5);
    st(function() {print('black', 'From ancient grudge break to new mutiny,');}, 3000*1.5);
    st(function() {print('black', 'Where civil blood makes civil hands unclean');}, 4000*1.5);
    st(function() {print('black', 'From forth the fatal loins of these two foes');}, 5000*1.5);
    st(function() {print('black', 'A pair of star-crossed lovers take their life,');}, 6000*1.5);
    st(function() {print('black', 'Whose misadventured piteous overthrows ');}, 7000*1.5);
    st(function() {print('black', "Doth with their death bury their parents' strife.");}, 8000*1.5);
    st(function() {print('black', 'The fearful passage of their death -marked love');}, 9000*1.5);
    st(function() {print('black', "And the continuance of their parents' rage,");}, 10000*1.5);
    st(function() {print('black', "Which, but their children's end, naught could remove,");}, 11000*1.5);
    st(function() {print('black', "Is now the two hours' traffic of our stage");}, 12000*1.5);
    st(function() {print('black', "That which, if you with patient ears attend,");}, 13000*1.5);
    st(function() {print('black', 'What here shall miss, our toil shall strive to mend.');}, 21000);
    st(function() {
        characters.pop();
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO23jhWeLBickkd4BV8YCCVa8uUesBQQKJ1Q&s';
        characters.push(sampson);
        characters.push(gregory);
        sampson.xvel = 1;
        gregory.xvel = .5;
        sampson.toupdate = true;
        gregory.toupdate = true;
    }, 22000);
    st(function() {
        sampson.xvel = 0;
        gregory.xvel = 0;
        print('red', 'Sampson: I can fight any Montague.');
        print('red', 'Gregory: I doubt you would.');
        characters.push(abram);
        abram.toupdate = true;
        abram.xvel = -1;
    }, 24000);
    st(function() {
        abram.xvel = 0;
        print('blue', 'Abram: Do you bite your thumb at us?');
        print('red', 'Sampson: No, I do not.');
        print('red', 'Sampson: Let us fight.');
        props.push(new sword(sampson, 'r'));
        props.push(new sword(gregory, 'r'));
        props.push(new sword(abram, 'l'));
        props[0].toupdate = true;
        props[1].toupdate = true;
        props[2].toupdate = true;
    }, 26000);
    st(function() {
        benvolio.toupdate = true;
        benvolio.x = wall;
        benvolio.xvel = -1.5;
        tybalt.toupdate = true;
        tybalt.xvel = 1.5;
    }, 30000);
    st(function() {
        benvolio.xvel = 0;
        tybalt.xvel = 0;
        print('blue', 'Benvolio: Part, fools! You know not what you do.');
        print('red', 'Tybalt: Turn thee, Benvolio, and look upon thy doom.');
        prince.toupdate = true;
        prince.xvel = 1;
    }, 32500);
    st(function() {
        props = [];
        prince.xvel = 0;
        print('green', 'Enemies of peace, I will kill you if you fight again!');
    }, 34000);
    st(function() {
        curtain = true;
        characters.pop();
        characters.pop();
        characters.pop();
        prince.toupdate = false;
        prince.x = 0;
        tybalt.toupdate = false;
        tybalt.x = 0;
        montague.x = 100;
        montague.toupdate = true;
        ladymont.x = 200;
        ladymont.toupdate = true;
    }, 36000);
    st(function() {
        curtain = false;
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBRu9pM67tYkrgkBt99mBn7A5-1-HvwN_baA&s';
        print('blue', 'Lady Capulet: Right glad I am that romeo was not at this fray. By the way, where is he?');
        print('blue', "Benvolio: Yeah, Romeo is super sad. Don't worry, I can find out why he is sad.");
    }, 37000);
    stsu(function() {
        curtain = true;
        ladymont.exit();
        montague.exit();
        romeo.x = 100;
        romeo.toupdate = true;
    }, 40000);
    stsu(function() {
        curtain = false;
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1r3-14IarBFZqR1aX30h_TV-5snJyk9FPnQ&s';
        print('blue', 'Benvolio: Good morrow cousin.');
        print('blue', 'Romeo: Is the day so young.');
        print('blue', 'Benvolio: Why are you so sad?');
    }, 40500);
    stsu(function() {
        print('blue', 'Romeo: I am in love with Rosaline, but she does not love me back.');
        characters.push(sampson);
        sampson.exit();
        sampson.enter(1.5);
    }, 44000);
    stsu(function() {
        sampson.stop();
        print('red', 'Peter: Hey, you, can you read this?');
        print('blue', 'Romeo: If I know the letters and know the language.');
        print('blue', 'Romeo: No, I am just kidding, I know how to read.');
    }, 45000);
    stsu(function() {
        print('blue', 'Romeo: It says you have to invite these people to a party.');
        print('red', 'Peter: Hey, thanks, if you be not Montagues, come and have some fun.');
    }, 48000);
    stsu(function() {
        print('blue', 'Benvolio: We should go.');
        print('blue', 'Romeo: Okay, but only because Rosaline will be there.')
    }, 50000);
    stsu(function() {
        curtain = true;
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBRu9pM67tYkrgkBt99mBn7A5-1-HvwN_baA&s';
        characters.pop();
        romeo.exit();
        benvolio.exit();
        capulet.toupdate = true;
        capulet.x = 100;
        paris.toupdate = true;
        paris.x = 400;
    }, 52000);
    stsu(function() {
        curtain = false;
        print('green', 'Paris: Can I marry your daughter.');
        print('red', 'Capulet: Dude, chill out, you guys can marry after two more years.');
    }, 53000);
    stsu(function() {
        curtain = true;
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1r3-14IarBFZqR1aX30h_TV-5snJyk9FPnQ&s';
        capulet.exit();
        paris.exit();
        romeo.place(300);
        benvolio.place(100);
        mercutio.place(500);
    }, 56000);
    stsu(function() {
        curtain = false;
        print('blue', 'Romeo: I do not want to come to this party, I had a dream that this party would lead to my death.');
        print('green', 'Mercutio: I see Queen Mab hath been with you tonight. She puts dreams of love in men.');
    }, 57000);
    stsu(function() {
        print('blue', 'Romeo: Okay, fine, I will go to the party.');
    }, 60000);
    stsu(function() {
        curtain = true;
        bg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBRu9pM67tYkrgkBt99mBn7A5-1-HvwN_baA&s';
        romeo.exit();
        mercutio.exit();
        benvolio.exit();
    }, 61000);
    stsu(function() {
        curtain = false;
        romeo.enter(1.5);
        juliet.enter(1.5, op=true);
    }, 62000);
    stsu(function() {
        romeo.stop();
        juliet.stop();
        print('blue', 'Romeo: If I profane with my unworthiest hand');
        print('blue', 'This holy shrine, the gentle sin is this:');
        print('blue', 'My lips, two blushing pilgrims, ready stand');
        print('blue', 'To smooth that rough touch with a tender kiss.');
    }, 63000);
    stsu(function() {
        print('red', 'Juliet: Good pilgrim, you do wrong your hand too much,');
        print('red', 'Which mannerly devotion shows in this,');
        print('red', "For saints have hands that pilgrims' hands do touch,");
        print('red', "And palm to palm is holy palmers' kiss.");
    }, 67000);
    stsu(function() {
        censored = true;
    }, 71000);
    stsu(function() {
        censored = false;
        print('blue', 'Romeo: Thus from my lips, by thine, my sin is purged.');
        print('red', "Juliet: You kiss by th' book.");
    }, 73000);
    stsu(function() {
        romeo.enter(-3);
    }, 75000);
    stsu(function() {
        romeo.stop();
        romeo.exit();
        nurse.enter(1.5);
    }, 76000);
    stsu(function() {
        nurse.stop();
        print('red', 'Juliet: Who was that?');
        print('gray', 'Nurse: That was Romeo Montague.');
        print('red', 'Juliet: My only love sprung from my only hate!');
    }, 77000);
    stsu(function() {
        curtain = true;
        juliet.exit();
        nurse.exit();
        tybalt.place(200);
        capulet.place(400);
    }, 80000);
    stsu(function() {
        curtain = false;
        print('red', 'Tybalt: Romeo, the Monatague was here.');
        print('red', 'Capulet: Are you sure?');
    }, 81000);
    stsu(function() {
        print('red', 'Tybalt: Yes, he did not even bother to wear red clothes to blend in!');
        print('red', 'I will kill him!');
    }, 83000);
    stsu(function() {
        print('red', 'Capulet: No, do not do this, everyone likes Romeo.');
        print('red', 'Tybalt: Okay, but I will get him another day.');
    }, 85000);
    stsu(function() {
        curtain = true;
        tybalt.exit();
        capulet.exit();
    }, 86000)
    latim = 86000*1.5;
}

function sword(of, facing) {
    if (facing === 'r') {
        this.x = of.x + 50;
        this.y = of.y + 15;
    } else {
        this.x = of.x - 50;
        this.y = of.y + 15;
    }
    this.xvel = of.xvel;
    this.yvel = of.yvel;
    this.update = function() {
        play.ctx.fillStyle = 'grey';
        play.ctx.fillRect(this.x, this.y, 50, 7);
    };
};

function background(src) {
    this.src = src;
    this.update = function() {
        this.img = new Image();
        this.img.src = this.src;
        play.ctx.drawImage(this.img, 0, 0, 1000, 400);
    }
}

function sprite(x, y, bcolr, gendr) {
    this.x = x;
    this.y = y;
    this.xvel = 0;
    this.yvel = 0;
    this.toupdate = false;
    this.bcolr = bcolr;
    this.gendr = gendr
    this.update = function() {
        play.ctx.fillStyle = bcolr;
        play.ctx.fillRect(this.x, this.y, 50, 100);
        play.ctx.fillRect(this.x, this.y + 100, 10, 50);
        play.ctx.fillRect(this.x + 40, this.y + 100, 10, 50);
        play.ctx.fillStyle = '#ffe5b4';
        play.ctx.fillRect(this.x + 8, this.y - 35, 35, 35);
        play.ctx.fillStyle = 'black';
        play.ctx.fillRect(this.x + 8, this.y - 40, 35, 5);
        if (this.gendr === 'w') {
            play.ctx.fillRect(this.x + 3, this.y - 40, 5, 50);
            play.ctx.fillRect(this.x + 40, this.y - 40, 5, 50);
        }
    };
    this.enter = function(vel, op=false) {
        if (op === true) {
            this.x = wall;
            vel *= -1;
        }
        this.xvel = vel;
        this.toupdate = true;
    };
    this.exit = function() {
        this.x = 0;
        this.toupdate = false;
    };
    this.place = function(x) {
        this.toupdate = true;
        this.x = x;
    };
    this.stop = function() {
        this.xvel = 0;
    };
};

function sleep(seconds) {
    const date = Date.now();
    do {currentDate = Date.now();
    } while (currentDate - date < seconds * 1000);
};

function print(colr, ...value) {
    if (colr === 'gray') {
        colr = 'black';
    }
    for (i = 0; i < value.length; i += 1) {String(value[i]);}
    value = value.join(" ");
    div = document.getElementById("output");
    text = document.createElement("p");
    text.setAttribute('style', 'color: ' + colr + ';');
    text.innerHTML = value;
    div.appendChild(text);
    text.scrollIntoView();
};

function stsu(func, tim) {
    st(func, tim*1.5);
};

function st(func, tim) {
    setTimeout(func, tim+latim);
};

function update() {
    play.clear();
    bg.update();
    for (let i = 0; i < characters.length; i++) {
        if (characters[i].toupdate === true) {
            characters[i].update();
        }
        characters[i].x += characters[i].xvel;
        characters[i].y += characters[i].yvel;
    }
    for (let i = 0; i < props.length; i++) {
        props[i].update();
        props[i].x += props[i].xvel;
        props[i].y += props[i].yvel;
    }
    for (let i = 0; i < rotated.length; i++) {
        rotated[i]();
    }
    if (curtain === true) {
        var curimg = new Image();
        curimg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJykvvGXDhdA-X8Y1ALubDtmnvel2B3dqIxA&s';
        play.ctx.drawImage(curimg, 0, 0, 1000, 400);
    }
    if (censored === true) {
        var censorimg = new Image();
        censorimg.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0WLufrGKqj0nfSpyj1atHxY24L6UndYz3KA&s';
        play.ctx.drawImage(censorimg, 0, 0, 1000, 400);
    }
};