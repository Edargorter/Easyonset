/* Doodle Stroll by Matt Frangakis and Zachary Bowditch 2019 */

#define no_blocks 3
#define env_length 16
#define env_width 2
#define min_dist 4
int player_x;
int player_y;
int count;
int score;
int dir;
int blocks[][2] = {{-1, -1}, {-1, -1}, {-1, -1}};
int counter;
bool gameover;
int ms = 50;
int active_blocks;

void setup() {
	player_x = 7;
	player_y = 0;
	gameover = false;
	count = 1;
  score = 0;
	active_blocks = 0;
	randomSeed(42);
}

void spawn_block(int i){
	int offset = blocks[(i - 1) % no_blocks][0];
	if(offset > min_dist)
		offset = 0;
	blocks[i][0] = random(16 + offset, 24 + offset);
	blocks[i][1] = random(0, 1);
}

void move_blocks(){
	for(int i = 0; i < no_blocks; i += 1){
		if(blocks[i][0] - 1 < 0){
			spawn_block(i);
      score++;
		} else
			blocks[i][0] -= 1;
	}		
}

void getDirection(){
}

void move_player(int x, int y){
	player_x = (player_x + 1) % env_width;
	player_y = (player_y + 1) % env_length;
}

void loop() {
  Serial.println("Score: " + String(score));
  delay(ms);

	if(count % (1000/ms)  == 0)
		move_blocks();

	if(count % (250/ms) == 0){
    getDirection();
		if(true)
			move_player(0, -1);	
		else if(true)
			move_player(0, 1);
		else if(true)
			move_player(-1, 0);
		else if(true)
			move_player(1, 0);
	}

	for(int i = 0; i < no_blocks; i += 1){
		if(player_x == blocks[i][0] && player_y == blocks[i][1]){
			gameover = true;
		}
	}

	if(gameover){
		setup();
		gameover = false;
	}	
}
