function casino() {
  c = 100;
  a = input("Welcome to the Casino. You have " + c.toString() + " dollars. We have an awesome selection of games for you to play. You can play the slot machine(type sm to play), the lottery(type lotto to play), roulette(type roulette to play), and blackjack(type blackjack to play). If you want to stop playing type end.", "str");
  if (a == "sm") {
    print("Play for 1 coin and a chance of winning 100 to 300 coins.");
    n = [];
    for (i = 0; i < 3; i += 1) {n.push(randint(1, 3));}
    for (i = 0; i < 5; i += 1) {
      print("...");
      sleep(1000);
    }
    print("The numbers are", n[0], n[1], n[2].toString() + ".");
    if (n[0] == n[1] && n[1] == n[2]) {
      print("You won.");
      w = randint(100, 300);
      c += w;
      print("You won", w, "dollars.");
    } else {
      print("You lose.");
      c -= 1;
    }
  }
  if (a == "blackjack") {
    print("Play for 5 coins and a chance to win 25 coins.");
    d = ["s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA"];
    sd = [];
    for (i = 0; i < d.length; i += 1) {
      ri = 0;
      m = 0;
      while (m < sd.length - 1) {
        m = 0;
        ri = randint(0, d.length - 1);
        for (i = 0; i < sd.length; i += 1) {
          if (sd[i] != d[ri]) {m = m + 1;}
        }
      }
      sd.push(d[ri]);
    }
    d = sd;
    ca = d[0];
    d[0] = d[d.length - 1];
    d[d.length - 1] = ca;
    p1 = [];
    p2 = [];
    [p1, d] = deal(p1, d, 2);
    [p2, d] = deal(p2, d, 2);
    p1ct = 0;
    while (true) {
      print("Your Cards: ");
      for (i = 0; i < p1.length; i += 1) {print(p1[i]);}
      print("Dealer's Card:", p2[0]);
      if (input("Type more for more cards or end to end the game: ",) == "end") {
        ap = 0;
        for (i = 0; i < p1.length; i += 1) {
          if (isLetter(i.slice(1)) == false) {p1ct = p1ct + +i.slice(1);
          } else {
            if (i.slice(1) == "J" || i.slice(1) == "Q" || i.slice(1) == "K") {p1ct = p1ct + 10;
            } else {
              if (i.slice(1) == "A") {
                if (ap == 0) {ap = input("Ace Point Value(1 or 11).", "int");}
                p1ct += ap;
              }
            }
          }
        }
        break;
      } else {[p1, d] = deal(p1, d, 1);}
    }
    if (p1ct > 21) {
      print("You Lose. You got over 21 points.");
      return c - 5;
    }
    while (true) {
      p2p = [];
      ac = 0;
      for (i = 0; i < p2.length; i += 1) {
        if (isLetter(p2[i].slice(1)) == false) {p2p.push(Number.parseInt(p2[i].slice(1)));
        } else {
          if (p2[i].slice(1) == "J" || p2[i].slice(1) == "Q" || p2[i].slice(1) == "K") {p2p.push(10);
          } else {
            if (p2[i].slice(1) == "A") {
              ac += 1;
              p2p.push(111);
            }
          }
        }
      }
      t = 0;
      for (i = 0; i < p2p.length; i += 1) {
        if (p2p[i] !== 111) {t += p2p[i];}
      }
      if (ac > 0) {
        if (t + ac * 11 > 21) {t += ac;
        } else {t += ac * 11;}
      }
      if (t < p1ct) {[p2, d] = deal(p2, d, 1);
      } else {
        if (t > 21) {
          print("You Win! The dealer got", t, "points.");
          c += 25;
          break;
        } else {
          if (t > p1ct) {
            print("You Lose. The dealer got", t, "points.");
            c -= 5;
            break;
          } else {
            if (t == 21 && t == p1ct) {
              print("You Tied. The dealer got", t, "points.");
              break;
            }
          }
        }
      }
    }
  }
  if (a == "lotto") {
    q = randint(25000000, 1500000000);
    print("Play for 2 dollars and mabye win", q, "dollars.");
    rn = [];
    pn = [];
    print("Choose six numbers form 1 to 50 in the spaces below.");
    for (i = 0; i < 6; i += 1) {
      rn.push(randint(1, 50));
      pn.push(input("Number " + (i + 1).toString() + ": ", "int"));
    }
    pn = sort(pn, []);
    rn = sort(rn, []);
    if (rn == pn) {
      print("You won", q, "dollars.");
      c += q;
    } else {
      print("You lose.");
      c -= 2;
    }
  }
  if (a == "roulette") {
    do {d = input("How much money do you want to bet?", "int");}
    while (d > c);
    n = randint(1, 10);
    if (input("Pick your number from 1 to 30.", "int") == n) {
      print("You win.");
      c += d;
    } else {
      print("You lose.");
      print("The number was...");
      sleep(1000);
      print(n);
      c -= d;
    }
  }
  if (a == "end") {
    print("Why did you press end. :(");
    print("Ending in:");
    for (i = 0; i < 3; i += 1) {
      print(3 - i);
      sleep(1000);
    }
    print("..... (beeeep)");
  }
  return c;
};
function sort(values, svalues) {
  if (values.length == 0) {return svalues;}
  min = 10000000;
  ind = 0;
  for (i = 0; i < values.length; i += 1) {
    if (values[i] < min) {
      min = values[i];
      ind = i;
    }
  }
  delete values[ind];
  svalues.push(min);
  return sort(values, svalues);
};
function deal(pd, d, cn) {
  for (i = 0; i < cn; i += 1) {
    j = 4 * i;
    pd.push(d[j]);
  }
  nd = [];
  for (i = 0; i < d.length_pj_a; i += 1) {
    if (i > cn) {nd.push(d[i]);}
  }
  return [pd, nd];
};
const isLetter = (chr) => (str.length === 1 && str.match(/[a-z]/i));
casino();