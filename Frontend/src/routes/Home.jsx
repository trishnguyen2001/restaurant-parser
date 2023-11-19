import styled from "styled-components";
import { useForm } from "react-hook-form";
import { SERVER_URL} from "api";
import React, {useState } from "react";

const Container = styled.main`
  width: 100vw;
  height: 110vh;
  display: flex;
  justify-content: center;
  margin-top: 36px;
`;

const InfoText = styled.div`
  text-align: center;
  font-size: 16px;
  font-weight: normal;
  padding: 10px 0;
  color: #293545;
`;

const Title = styled.div`
  text-align: center;
  font-size: 48px;
  font-weight: bold;
  padding: 50px 0 10px;
  color: #293545;
`;

const ErrorText = styled.span`
  color: #cf316a;
  font-size: 14px;
  margin-top: 5px;
  display: flex;
`;

const Input1 = styled.input`
  margin-top: 15px;
  width: 500px;
  padding: 10px;
  border: 1px solid #b0b0b0;
  border-radius: 20px;
  height: 37px;
  color: #888888;
  font-size: 16px;
  font-weight: 400;
`;

const SubmitButton = styled.button`
  margin-top: 30px;
  width: 500px;
  height: 44px;
  padding: 15px;
  margin-bottom: 100px;
  border-radius: 20px;
  background-color: #84b8bf;
  color: #ffffff;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color:
            #79dbe8
  ;
  }
`;

const RightSide = styled.div`
  border-style: solid;
  border-radius: 10px;
  color: #293545;
`;

function Home() {
  const [isFetching, setIsFetching] = useState(false);
  const [userPrompt, setUserPrompt] = useState("");
  const [serverError, setServerError] = useState({ status: 0, message: "" });


  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();

  const onSubmit = async () => {
      const body = {
        userPrompt: userPrompt,
      };
      console.log(`body = ${JSON.stringify(body)}`);

      setIsFetching(true);
      const response = await fetch(
          `${SERVER_URL}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
        }
      );
      console.log("Request sent to Flask server. Waiting for response...");
      const data = await response.json();
      console.log(response.status, data);
      setServerError({ status: response.status, message: data.message });

      if (response.ok) {
        alert(data);
      }
      setIsFetching(false); 
  };


  return (
    <>
      <Container>
        <RightSide>
          <div
            style={{
              borderBottom: "1px solid #888",
              paddingBottom: "30px",
              width: "500px ",
            }}
          >

            <Title>Welcome to Restaurant Parser!</Title>
            <InfoText>
              Please input your instructions in the box below!
            </InfoText>
          </div>



            <div>
              <form onSubmit={onSubmit}>
                  <div style={{ flex: 1 }}>
                    <Input1
                      {...register("userPrompt",
                          {
                                required: "Input is required",
                            },
                      )}
                      style={{ color: "black" }}
                      name="userPrompt"
                      value={userPrompt}
                      onChange={(e) => setUserPrompt(e.target.value)}
                    />
                    {errors.userPrompt && (
                      <ErrorText className="error-text">
                        <span>{errors.userPrompt.message.toString()}</span>
                      </ErrorText>
                    )}
                  </div>
              </form>
                </div>
                <div>
                {serverError && (
                  <ErrorText className="error-text">
                    <span>{serverError.message}</span>
                  </ErrorText>
                )}
                <SubmitButton type="submit">
                  Submit
                </SubmitButton>
            </div>
        </RightSide>
      </Container>
    </>
  );
}

export default Home;
