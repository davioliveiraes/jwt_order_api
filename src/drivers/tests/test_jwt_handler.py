import pytest
import jwt
from src.drivers.jwt_handler import JwtHandler
from src.configs.jwt_configs import jwt_infos 
   
                                                
@pytest.fixture 
def jwt_handler():
    return JwtHandler()
                                                
   
class TestCreateToken:                        
    def test_create_token_returns_string(self, jwt_handler):
        token = jwt_handler.create_token(1, "davi")                                       
        assert isinstance(token, str)
                                                
    def test_create_token_contains_user_data(self, jwt_handler):
        token = jwt_handler.create_token(1, "davi")                                       
   
        decoded = jwt.decode(                 
            token,
            jwt_infos["KEY"],
            algorithms=[jwt_infos["ALGORITHM"]]           
          )
                                                
        assert decoded["user_id"] == 1
        assert decoded["username"] == "davi"
        assert "exp" in decoded
                                                
    def test_different_users_generate_different_tokens(self, jwt_handler):                  
        token1 = jwt_handler.create_token(1, "davi")
        token2 = jwt_handler.create_token(2, "ana")                                        
   
        assert token1 != token2               
                  

class TestDecodeToken:
    def test_decode_valid_token(self, jwt_handler):                                 
        token = jwt_handler.create_token(1, "davi")                                       
                  
        result = jwt_handler.decode_token(token)

        assert result["user_id"] == 1         
        assert result["username"] == "davi"
                                                
    def test_decode_invalid_token(self, jwt_handler):
        with pytest.raises(jwt.InvalidTokenError):         
            jwt_handler.decode_token("token_invalido_123")
                  
    def test_decode_token_signed_with_different_key(self, jwt_handler):
        fake_token = jwt.encode({
                "user_id": 1, 
                "username": "hacker"
            }, 
            "chave_errada",                   
            algorithm=jwt_infos["ALGORITHM"]
          )                                     
   
        with pytest.raises(jwt.InvalidSignatureError):
            jwt_handler.decode_token(fake_token)