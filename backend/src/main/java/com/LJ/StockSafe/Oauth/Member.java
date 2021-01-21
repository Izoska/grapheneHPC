package com.LJ.StockSafe.Oauth;

import lombok.Builder;
import lombok.Getter;

@Getter
//@Entity
public class Member {
//    @Id
//    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String oauthId;

    private String name;

    private String email;

    private String imageUrl;


    protected Member() {
    }

    @Builder
    public Member(Long id, String oauthId, String name, String email, String imageUrl) {
        this.id = id;
        this.oauthId = oauthId;
        this.name = name;
        this.email = email;
        this.imageUrl = imageUrl;
    }

    public Member update(String name, String email, String imageUrl) {
        this.name = name;
        this.email = email;
        this.imageUrl = imageUrl;
        return this;
    }
}