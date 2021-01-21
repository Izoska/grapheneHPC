
package com.LJ.StockSafe.Oauth;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class LoginResponse {
    private Long id;
    private String name;
    private String email;
    private String tokenType;
    private String accessToken;
    private String refreshToken;
    private String imageUrl;

    @Builder
    public LoginResponse(Long id, String name, String email, String tokenType, String accessToken, String refreshToken) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.tokenType = tokenType;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }

    @Builder
    public LoginResponse(Long id, String name, String email, String imageUrl, String tokenType, String accessToken, String refreshToken) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.imageUrl = imageUrl;
        this.tokenType = tokenType;
        this.accessToken = accessToken;
        this.refreshToken = refreshToken;
    }

}