# ms_word_auto

    log.info("++++++++++++++++++++++++++++++");
    if (message.getCommonConditions() != null) {
      Map<String, Object> regex = StringUtils.regexMap(commonConditions);
      ObjectMapper oMapper = new ObjectMapper();
      if (regex.get("searchField").equals("cntrctNo")) {
        resultList =
            resultList.stream().filter(d -> d.getCntrctId().equals(regex.get("searchValue")))
                .collect(Collectors.toList());
      } else if (regex.get("searchField") != null) {
        resultList =
            resultList
                .stream().filter(d -> oMapper.convertValue(d, Map.class)
                    .get(regex.get("searchField")).equals(regex.get("searchValue")))
                .collect(Collectors.toList());
      }

      log.info(resultList.toString());

      List<ControlSendHist> re = new ArrayList<>();
      if (regex.get("startDate") != "" & regex.get("endDate") != "") {
        for (ControlSendHist c : resultList) {
          DateFormat formater = new SimpleDateFormat("yyyyMMdd");
          Calendar startCalendar = Calendar.getInstance();
          Calendar endCalendar = Calendar.getInstance();
          Calendar curCalendar = Calendar.getInstance();
          try {
            regex.put("startDate", ((String) regex.get("startDate")).replace("-", ""));
            regex.put("endDate", ((String) regex.get("endDate")).replace("-", ""));
            if (c.getRegDate().length() > 8) {
              c.setRegDate(c.getRegDate().replace("-", ""));
              c.setRegDate(c.getRegDate().substring(0, 8));
            }

            curCalendar.setTime(formater.parse(c.getRegDate()));
            startCalendar.setTime(formater.parse((String) regex.get("startDate")));
            endCalendar.setTime(formater.parse((String) regex.get("endDate")));

            if (curCalendar.equals(startCalendar)
                | (curCalendar.after(startCalendar) && curCalendar.before(endCalendar))
                | curCalendar.equals(endCalendar)) {
              re.add(c);
            }
          } catch (ParseException e) {
            e.printStackTrace();
          }
        }
        resultList = re;
      }

      log.info(resultList.toString());

      if (regex.get("startNo") != null & regex.get("endNo") != null) {
        if (resultList.size() > 0
            & resultList.size() > Integer.parseInt((String) regex.get("endNo"))) {
          resultList = resultList.subList(Integer.parseInt((String) regex.get("startNo")),
              Integer.parseInt((String) regex.get("endNo")) + 1);
        } else {
          resultList = resultList.subList(Integer.parseInt((String) regex.get("startNo")),
              resultList.size());
        }
      }

      log.info(resultList.toString());

      if (regex.get("orderFieldName") != null & regex.get("orderDirection") != null) {
        String orderFieldName = regex.get("orderFieldName") == "cntrctNo" ? "ctrctId"
            : (String) regex.get("orderFieldName");
        if (regex.get("orderDirection") == "A") {

        } else if (regex.get("orderDirection") == "D") {

        }
      }
    }

    log.info("++++++++++++++++++++++++++++++");
////////////////////////////////////////////////////////////////////////////////////////////

@ApiResponses(
      value = {@ApiResponse(code = 200, message = "", response = FirmwareBaseInfoDTO.class)})
  @ApiOperation(value = "디바이스 송신 이력 정보 조회", hidden = false)
  @PostMapping("/retrieveDeveiceSendHist")
//////////////////////////////////////////////////////////////////////////////////////////
@ApiModelProperty(value = "시작일자", required = false, hidden = false, example = "2019-09-03")
  String startDate;
  @ApiModelProperty(value = "종료일자", required = false, hidden = false, example = "2019-09-04")
  String endDate;
  @ApiModelProperty(value = "정렬기준 필드명", required = false, hidden = false, example = "cntrctNo")
  String orderFieldName;

  /////////////////////////////////////////////////////////////////////////////////////////
