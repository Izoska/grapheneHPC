package com.LJ.StockSafe.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.MailException;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

import com.LJ.StockSafe.model.dto.MemberDto;
import com.LJ.StockSafe.model.mapper.MemberMapper;

@Service
public class MemberServiceImpl implements MemberService{
	
	@Autowired
	MemberMapper memberMapper;
	
	@Autowired
	JavaMailSender javamailSender;

	@Override
	public boolean createMember(MemberDto memberdto) {
		// TODO 