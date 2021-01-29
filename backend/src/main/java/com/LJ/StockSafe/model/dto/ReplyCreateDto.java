package com.LJ.StockSafe.model.dto;

public class ReplyCreateDto {
	private int id;
	private String stockId;
	private String replyContent;
	private String memberId;
	private String replyRegdate;
	private int replyLevel;
	private int replyParent;
	
	public ReplyCreateDto() {
		super();
	}
	public ReplyCreateDto(int id, String stockId, String replyContent, String memberId, String replyRegdate, int replyLevel,
			int replyParent) {
		super();
		this.id = id;
		this.stockId = stockId;
		this.replyContent = replyContent;
		this.memberId = memberId;
		this.replyRegdate = replyRegdate;
		this.replyLevel = replyLevel;
		this.replyParent = replyParent;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getStockId() {
		return stockId;
	}
	public void setStockId(String stockId) {
		this.stockId = stockId;
	}
	public String getReplyContent() {
		return replyContent;
	}
	public void setRep