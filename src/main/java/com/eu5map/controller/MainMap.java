package com.eu5map.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;



@Controller
public class MainMap {

    @GetMapping(path = "/index")
    public String index(){

        return "index";
    }
}
