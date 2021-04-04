const {Engine, Render, Runner, World, Bodies, Body, Events} = Matter;
const engine = Engine.create ();
const {world} = engine;
let render;
let runner;
let robot;
const unitLengthX = 110;
const unitLengthY = 110;


function table (graph) {
  const cellsHorizontal = 5;
  const cellsVertical = 5;
  const width = cellsHorizontal * 110;
  const height = cellsVertical * 110;
 
  engine.world.gravity.y = 0;
  render = Render.create ({
    element: document.body,
    engine: engine,
    options: {
      wireframes: false,
      width,
      height,
      wireframes: false,
      background: '#f8f5f1'
      // background : '#bbdfc8',
    },
  });
  Render.run (render);
  runner = Runner.create ();
  Runner.run (runner, engine);

  const walls = [
    Bodies.rectangle (width / 2, 0, width, 2, {isStatic: true}),
    Bodies.rectangle (0, height / 2, 2, height, {isStatic: true}),
    Bodies.rectangle (width, height / 2, 2, height, {isStatic: true}),
    Bodies.rectangle (width / 2, height, width, 2, {isStatic: true}),
  ];
  World.add (world, walls);


  for(const [key , value] of Object.entries(graph)){
    let indexRow = parseInt(key.charAt(0))
    let indexColumn = parseInt(key.charAt(1))
    let type = value[0];
    if (type === 'r') {
         robot = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX,
        unitLengthY,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: './images/robot.png',
              xScale: 0.7,
              yScale: 0.7,
            },
          },
        }
      );
      World.add (world, robot);
    } else if (type === 'x') {
      const cake = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX - 10,
        unitLengthY - 10,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: randomPic(),
            },
          },
        }
      );
      World.add (world, cake);
    } else if (type === 'p') {
      const dest = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX - 10,
        unitLengthY - 10,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: './images/goal.png',
            },
          },
        }
      );
      World.add (world, dest);
    } else if (type === 'b') {
      const butter = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX,
        unitLengthY,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: './images/butter.png',
              xScale: 0.08,
              yScale: 0.08
            },
          },
        }
      );
      World.add (world, butter);
    }

  }
}



function randomPic(){
  let rand = Math.floor(Math.random() * 5)
  if(rand === 0) return "./images/cake.png";
  else if(rand === 1) return "./images/noodle.png";
  else if(rand === 2) return "./images/noodles.png";
  else if(rand === 3) return "./images/watermelon.png";
  else if(rand === 4) return "./images/taco.png";

}


function showResults(path){
  let index = 0;
  let id = setInterval(function(){
    if(index === path.length -1){
      clearInterval(id)
    }
    let key = path[index];
    let indexRow = parseInt(key.charAt(0));
    let indexColumn = parseInt(key.charAt(1));
    Body.setPosition(robot ,{x : (indexColumn + 0.5) * unitLengthX  ,y:(indexRow + 0.5) * unitLengthY} , {x: 0, y: 0.5});
    index ++;
  } , 1000);
}


async function run(){
  let resultsJSON = await eel.runIDS()();
  let result = JSON.parse(resultsJSON)
  table (result["graph"]);
  showResults(result["path"]);
}

run()