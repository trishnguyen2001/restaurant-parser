import styled from "styled-components";
import { useForm } from "react-hook-form";
import { SERVER_URL, parseUserInstr } from "api";
import React, { useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Ellipsis } from "react-spinners-css";

const Container = styled.main`
  width: 100vw;
  height: 110vh;
  display: flex;
  justify-content: center;
  margin-top: 36px;
`;

const LeftBox = styled.div`
  margin-top: 40px;
  margin-left: 50px;
  display: flex;
  justify-content: flex-start; /* Align items to the left */
  align-items: center; /* Center vertically */
  //margin-bottom: 20px; /* Add some spacing from the form */
`;

const Back = styled.div`
  font-size: 16px;
  font-weight: bold;
  //margin: 50px 0;
  //margin-bottom: 20px;
  color: #293545;
  cursor: pointer;
`;

const BookingRequest = styled.div`
  font-size: 26px;
  font-weight: bold;
  padding: 20px 0;
  color: #293545;
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

const Card = styled.div`
  border: 1px solid #293545;
  border-radius: 10px;
  padding: 10px;
  color: #293545;
  width: 390px;
  display: block;
  margin-right: 200px;
  margin-top: 150px;
`;

const LeftSide = styled.div`
  border-style: solid;
  border-radius: 10px;
  color: #293545;
  margin-right: 100px;
`;

const RightSide = styled.div`
  border-style: solid;
  border-radius: 10px;
  color: #293545;
`;

const Image = styled.div`
  padding: 15px;
  height: 250px;

  img {
    width: 100%;
    height: 100%;
    border-radius: 10px;
  }
`;

const Pricing = styled.div`
  margin-top: 10px;
  margin-left: 20px;
  font-size: 20px;
  font-weight: bold;
`;

const CostAndAmount = styled.div`
  margin-top: 20px;
  margin-left: 20px;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const Amount = styled.div`
  margin-right: 20px;
  font-size: 16px;
  font-weight: normal;
`;

const Total = styled.div`
  margin-top: 60px;
  margin-left: 20px;
  margin-bottom: 20px;
  font-size: 20px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const TotalCost = styled.div`
  margin-right: 20px;
  font-size: 20px;
  font-weight: bold;
`;

const ErrorMessageArea = styled.div`
  font-size: 12px;
  font-weight: 400;
  color: rgba(207, 49, 106, 1);
  margin-left: 200px;
`;

function Home() {
  const navigate = useNavigate();
  const location = useLocation();
  const [isFetching, setIsFetching] = useState(false);
  const [userPrompt, setUserPrompt] = useState("");
  const [serverError, setServerError] = useState({ status: 0, message: "" });
  const applyInputRef = useRef(null);


  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm();

  const onSubmit = async (formData) => {
      const body = {
        ...formData,
        userPrompt: userPrompt,
      };
      setIsFetching(true);
      const response = await fetch(
          `${SERVER_URL}/prompt=${prompt}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
        }
      );

      const data = await response.json();
      console.log(response.status, data);
      setServerError({ status: response.status, message: data.message });

      if (response.ok) {
        if (data.error) setServerError({ ...serverError, message: data.error });
        else navigate("success");
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
                <SubmitButton id="submitBooking-btn" type="submit">
                  Submit
                </SubmitButton>
            </div>
        </RightSide>
      </Container>
    </>
  );
}

export default Home;
