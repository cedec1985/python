import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import React, {useState,useEffect} from 'react';
import ReactDOM from 'react-dom';

/*function MyList(props){    //listItem
    const arr=props.data;
    const listItems=arr.map((val)=>
    <li>{val}</li>
    );
    return <ul>{listItems}</ul>;
}
const arr=["A","B","C"];
const el=<MyList data={arr} />;
ReactDOM.render(
    el,
    document.getElementById('root')
);*/
/*function AddForm () {
    const [sum, setSum] = useState(0);
    const [num, setNum] = useState(0);

    function handleChange(e){
        setNum(e.target.value);
    }
    function handleSubmit(e){
        setSum(sum+Number(num));
        e.preventDefault();
    }
    return <form onSubmit={handleChange}>
        <input type="number" value={num}
        onChange={handleChange} />
        <input type="submit" value="Add" />
        <p>Sum is {sum}</p>
        </form>;}
const el=<AddForm />;
ReactDOM.render(
    el,
    document.getElementById('root')
);*/
/*function Converter (){
    const[km,setKm]=useState(0);

    function handleChange(e){
        setKm(e.target.value);
    }
    function convert(km){
        return (km/1.609).toFixed(2);
    }
    return <div>
        <input type="text" value={km} onChange={handleChange} />
        <p>{km} km is {convert(km)} miles</p>
    </div>;
}
const el=<Converter />;
ReactDOM.render(
    el,
    document.getElementById('root')
);*/

/*</button>
function Counter(){
    const[counter, setCounter] = useState(0);

    useEffect(() => {                                 //useffect
        alert("number of clicks:"+counter);
    });
        function increment(){
            setCounter(counter+1);
    }
        return <div>
        <p>{counter}</p>
        <button onClick={increment}
        >Increment</button>
        </div>;
}
    const el =<Counter />;
    ReactDOM.render(
        el,
        document.getElementById('root')
);*/
/*class Counter extends React.Component {
    state = {
        counter: 0
    }
    increment = () => {
        this.setState({
            counter:
                this.state.counter + 1
        });
    }*/
/*componentDidMount(){              //componentDidMount and componentDidUpdate
this.setState({counter:42});}
componentDidUpdate(){
    alert("number of clicks:" +
  this.state.counter);}
render() {
  return <div>
  <p>{this.state.counter}</p>
  <button onClick={this.increment}
  >increment
  </button>
  </div>;
    }
}
const eloi = <Counter />;
ReactDOM.render(
    eloi,
    document.getElementById('root')
);*/

/*function Counter(){     //hooks in Counter App
    const[counter,setCounter]=
useState(0);
function increment(){
    setCounter(counter+1);
}
return <div>
    <p>{counter}</p>
    <button onClick={increment}>
        Increment
    </button>
    </div>;
}
const el =<Counter />;
ReactDOM.render(
    el,
    document.getElementById('root')
);
/*function Hello(){         //Hooks
   const[name,setName]= useState("albert");   return <h1>Hello {name}.</h1>//}
    /*nst elb =<Hello />;
    ReactDOM.render(
        elb,
        document.getElementById('root'));

    /*class B extends React.Component {   //state
        state = {
            name: "james"
        }
        render(){
            return <h1>Hello {this.state.name}.</h1>;
        }
    }
    const ceil = <B/>;
    ReactDOM.render(
        ceil,
        document.getElementById('root')
    );
    /*const name="cédric";
    const eld=<p>salut,{name}</p>;

    ReactDOM.render(
      eld,
      document.getElementById('root'));

    function F(props) {         //argument props in functional components
        return <p>Hello,{props.name}!</p>;
    }
    /*function Still (){   //components using components
        return <div>
            <F name="cédric"/>
            <F name="bertrand" />
            <F name="alain" />
            <F name="bernard" />
        </div>;
    }
    const el =<Still />;
    ReactDOM.render(
        el,
        document.getElementById('root')
    );

    /*let counter =0;
    function show(){
        counter++;
        const el =<p>{counter}</p>;
        ReactDOM.render(
            el, document.getElementById('root')
        );
    }
    setInterval(show,10000);

    class Counter extends React.Component {
        state = {
            counter: 0
        }
        increment = () => {
            this.setState({
                counter:
                    this.state.counter + 1
            });
        }
        render() {
            return <div>
                <p>{this.state.counter}</p>
                <button onClick={this.increment}
                >increment
                </button>
            </div>;
        }
    }
    const eloi = <Counter />;
    ReactDOM.render(
        eloi,
        document.getElementById('root')
    );*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
