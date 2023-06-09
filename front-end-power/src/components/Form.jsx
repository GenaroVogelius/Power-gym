import { csrftoken } from "./CSRFToken";



function Form({ setUserData, setNotFound, setIsLoading }) {


  const URL = "https://power-gym.onrender.com/"

  // URL FOR DEVELOP
  // const URL = "http://localhost:8000/"
  
  function handleSubmit(event) {
    setIsLoading(true)
    event.preventDefault()
    // ? como le pusiste un name al input asi lo podes llamar despues del .target
    let input = event.target.input_dni;
    let inputValue = event.target.input_dni.value
    const getUserState = async () => {

      try {
        const response = await fetch(
          `${URL}usuario/${inputValue}`
        );
        const data = await response.json();
        setIsLoading(false)
        
        if ("not found" in data) {
          setNotFound(true);
          input.value = "";
        } else {
          setUserData(data);
          // inputValue = "" no te funciona por eso hiciste la variable input
          input.value = "";
        }
      } catch (error) {
        console.log("Error:", error.message);
      }
    }
    getUserState()


    fetch(`${URL}usuario/${inputValue}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    });
  }


    return (
      <form onSubmit={handleSubmit}>
        <div class="user-box">
          <label>Ingrese su D.N.I</label>
          <input
            className="input"
            type="text"
            required
            name="input_dni"
            autoFocus
            autoComplete="off"
          />
        </div>
      </form>
    );

}

export default Form;